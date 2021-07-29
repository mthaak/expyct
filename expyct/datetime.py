import typing
from dataclasses import dataclass
from datetime import datetime, date, time, timedelta, timezone

from expyct import MapBefore


@dataclass
class DateTime(MapBefore):
    equals: typing.Optional[datetime] = None
    after: typing.Optional[datetime] = None
    before: typing.Optional[datetime] = None

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if self.equals is not None:
            return other == self.equals
        if not type(other) == datetime:
            return False
        if self.after is not None and not other > self.after:
            return False
        if self.before is not None and not other < self.before:
            return False
        return True


@dataclass
class Date(MapBefore):
    equals: typing.Optional[date] = None
    after: typing.Optional[date] = None
    before: typing.Optional[date] = None

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if self.equals is not None:
            return other == self.equals
        if not type(other) == date:
            return False
        if self.after is not None and not other > self.after:
            return False
        if self.before is not None and not other < self.before:
            return False
        return True


@dataclass
class Time(MapBefore):
    equals: typing.Optional[time] = None
    after: typing.Optional[time] = None
    before: typing.Optional[time] = None

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if self.equals is not None:
            return other == self.equals
        if not type(other) == time:
            return False
        if self.after is not None and not other > self.after:
            return False
        if self.before is not None and not other < self.before:
            return False
        return True


@dataclass
class AnyDateTime(MapBefore):
    equals: typing.Optional[typing.Union[datetime, date, time]] = None
    after: typing.Optional[typing.Union[datetime, date, time, timedelta]] = None
    before: typing.Optional[typing.Union[datetime, date, time, timedelta]] = None

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not (isinstance(other, datetime) or isinstance(other, date) or isinstance(other, time)):
            return False
        if self.equals is not None:
            return other == self.equals
        if self.after is not None:
            after = self._handle_timedelta(self.after)
            try:
                coerced_other, after = self._coerce_types(other, after)
            except ValueError:
                return False
            else:
                if not coerced_other > after:
                    return False
        if self.before is not None:
            before = self._handle_timedelta(self.before)
            try:
                coerced_other, before = self._coerce_types(other, before)
            except ValueError:
                return False
            else:
                if not coerced_other < before:
                    return False
        return True

    @staticmethod
    def _handle_timedelta(
        bound: typing.Union[datetime, date, time, timedelta]
    ) -> typing.Union[datetime, date, time]:
        """When timedelta is passed, it is used as a time relative to when
        the assertion is executed."""
        if isinstance(bound, timedelta):
            return datetime.now().astimezone(timezone.utc) + bound
        else:
            return bound

    @staticmethod
    def _coerce_types(other, bound):
        """Makes the types of bound and other equal, if possible."""

        def error():
            raise ValueError(f"Cannot coerce types {type(bound)} and {type(other)}")

        return {
            (datetime, datetime): lambda: (other, bound),
            (datetime, date): lambda: (other.date(), bound),
            (datetime, time): lambda: error(),
            (date, datetime): lambda: error(),
            (date, date): lambda: (other, bound),
            (date, time): lambda: error(),
            (time, datetime): lambda: error(),
            (time, date): lambda: error(),
            (time, time): lambda: (other, bound),
        }[(type(other), type(bound))]()


def parse_isoformat(dt):
    if isinstance(dt, str):
        try:
            return date.fromisoformat(dt)
        except ValueError:
            try:
                return time.fromisoformat(dt)
            except ValueError:
                return datetime.fromisoformat(dt).astimezone(timezone.utc)
    raise ValueError("Only str is allowed")


# before=timedelta(microseconds=1) to allow current time
LAST_SECOND = AnyDateTime(after=timedelta(seconds=-1), before=timedelta(microseconds=1))
LAST_MINUTE = AnyDateTime(after=timedelta(minutes=-1), before=timedelta(microseconds=1))
LAST_HOUR = AnyDateTime(after=timedelta(hours=-1), before=timedelta(microseconds=1))
LAST_DAY = AnyDateTime(after=timedelta(days=-1), before=timedelta(microseconds=1))
LAST_WEEK = AnyDateTime(after=timedelta(weeks=-1), before=timedelta(microseconds=1))
LAST_YEAR = AnyDateTime(after=timedelta(days=-365), before=timedelta(microseconds=1))
LAST_SECOND_ISO = AnyDateTime(
    after=timedelta(seconds=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_MINUTE_ISO = AnyDateTime(
    after=timedelta(minutes=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_HOUR_ISO = AnyDateTime(
    after=timedelta(hours=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_DAY_ISO = AnyDateTime(
    after=timedelta(days=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_WEEK_ISO = AnyDateTime(
    after=timedelta(weeks=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_YEAR_ISO = AnyDateTime(
    after=timedelta(days=-365), before=timedelta(microseconds=1), map_before=parse_isoformat
)

# LAST_MINUTE_ISOFORMAT
# TODO:
# THIS_MINUTE
# THIS_HOUR
THIS_DAY = AnyDateTime(
    after=date.today() - timedelta(days=1),
    before=date.today() + timedelta(days=1),
)
TODAY = THIS_DAY
# THIS_DAY / TODAY
# THIS_WEEK
# THIS_MONTH
# THIS_YEAR

THIS_DAY_ISO = AnyDateTime(
    after=date.today() - timedelta(days=1),
    before=date.today() + timedelta(days=1),
    map_before=parse_isoformat,
)
TODAY_ISO = THIS_DAY_ISO

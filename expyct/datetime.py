import typing
from dataclasses import dataclass
from datetime import datetime, date, time, timedelta, timezone

from expyct.base import Equals, MapBefore, Predicate, Instance

T = typing.TypeVar("T")


@dataclass
class AfterBefore(typing.Generic[T]):
    """Match a `date`, `time`, or `datetime` only if it takes place after and/or
    before given timestamps."""

    after: typing.Optional[T] = None
    before: typing.Optional[T] = None

    def __eq__(self, other):
        if self.after is not None and not other > self.after:
            return False
        if self.before is not None and not other < self.before:
            return False
        return True


@dataclass
class DateTime(MapBefore, Equals[datetime], AfterBefore[datetime], Predicate):
    """Any `datetime` object."""

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not type(other) == datetime:
            return False
        if not Equals.__eq__(self, other):
            return False
        if not AfterBefore.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


@dataclass
class Date(MapBefore, Equals[date], AfterBefore[date], Predicate):
    """Any `date` object."""

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not type(other) == date:
            return False
        if not Equals.__eq__(self, other):
            return False
        if not AfterBefore.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


@dataclass
class Time(MapBefore, Equals[time], AfterBefore[time], Predicate):
    """Any `time` object."""

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not type(other) == time:
            return False
        if not Equals.__eq__(self, other):
            return False
        if not AfterBefore.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


@dataclass
class DateOrTime(
    MapBefore, Equals[typing.Union[datetime, date, time, timedelta]], Instance, Predicate
):
    # after / before is a bit more complicated in this case
    # because there can be disparity between the types
    after: typing.Optional[typing.Union[datetime, date, time, timedelta]] = None
    before: typing.Optional[typing.Union[datetime, date, time, timedelta]] = None

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not (isinstance(other, datetime) or isinstance(other, date) or isinstance(other, time)):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Instance.__eq__(self, other):
            return False
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
        if not Predicate.__eq__(self, other):
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


def parse_isoformat(dt: str) -> typing.Union[date, time, datetime]:
    """Parse a ISO8601 string as a `date`, `datetime` or `datetime` object.

    Args:
        dt : the date/time string to parse
    """
    if isinstance(dt, str):
        try:
            return date.fromisoformat(dt)
        except ValueError:
            try:
                return time.fromisoformat(dt)
            except ValueError:
                return datetime.fromisoformat(dt).astimezone(timezone.utc)
    raise ValueError("Only str is allowed")


ANY_DATETIME = DateTime()
ANY_DATE = Date()
ANY_TIME = Time()

ANY_DATETIME_ISO = DateTime(map_before=parse_isoformat)
ANY_DATE_ISO = Date(map_before=parse_isoformat)
ANY_TIME_ISO = Time(map_before=parse_isoformat)

# before=timedelta(microseconds=1) to allow current time
LAST_SECOND = DateOrTime(after=timedelta(seconds=-1), before=timedelta(microseconds=1))
LAST_MINUTE = DateOrTime(after=timedelta(minutes=-1), before=timedelta(microseconds=1))
LAST_HOUR = DateOrTime(after=timedelta(hours=-1), before=timedelta(microseconds=1))
LAST_DAY = DateOrTime(after=timedelta(days=-1), before=timedelta(microseconds=1))
LAST_WEEK = DateOrTime(after=timedelta(weeks=-1), before=timedelta(microseconds=1))
LAST_YEAR = DateOrTime(after=timedelta(days=-365), before=timedelta(microseconds=1))
LAST_SECOND_ISO = DateOrTime(
    after=timedelta(seconds=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_MINUTE_ISO = DateOrTime(
    after=timedelta(minutes=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_HOUR_ISO = DateOrTime(
    after=timedelta(hours=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_DAY_ISO = DateOrTime(
    after=timedelta(days=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_WEEK_ISO = DateOrTime(
    after=timedelta(weeks=-1), before=timedelta(microseconds=1), map_before=parse_isoformat
)
LAST_YEAR_ISO = DateOrTime(
    after=timedelta(days=-365), before=timedelta(microseconds=1), map_before=parse_isoformat
)

# LAST_MINUTE_ISOFORMAT
# TODO:
# THIS_MINUTE
# THIS_HOUR
#: A date, time or datetime occurring on the current day
THIS_DAY = DateOrTime(
    after=date.today() - timedelta(days=1),
    before=date.today() + timedelta(days=1),
)
#: The same as THIS_DAY
TODAY = THIS_DAY
# THIS_DAY / TODAY
# THIS_WEEK
# THIS_MONTH
# THIS_YEAR

#: A ISO8601-formatted timestamp occurring on the current day
THIS_DAY_ISO = DateOrTime(
    after=date.today() - timedelta(days=1),
    before=date.today() + timedelta(days=1),
    map_before=parse_isoformat,
)
#: The same as THIS_DAY_ISO
TODAY_ISO = THIS_DAY_ISO

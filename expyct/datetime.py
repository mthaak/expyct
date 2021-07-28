import typing
from dataclasses import dataclass
from datetime import datetime, date, time, timedelta


@dataclass
class DateTime:
    after: typing.Optional[datetime] = None
    before: typing.Optional[datetime] = None

    def __eq__(self, other):
        if not type(other) == datetime:
            return False
        if self.after and not other > self.after:
            return False
        if self.before and not other < self.before:
            return False
        return True


@dataclass
class Date:
    after: typing.Optional[date] = None
    before: typing.Optional[date] = None

    def __eq__(self, other):
        if not type(other) == date:
            return False
        if self.after and not other > self.after:
            return False
        if self.before and not other < self.before:
            return False
        return True


@dataclass
class Time:
    after: typing.Optional[time] = None
    before: typing.Optional[time] = None

    def __eq__(self, other):
        if not type(other) == time:
            return False
        if self.after and not other > self.after:
            return False
        if self.before and not other < self.before:
            return False
        return True


@dataclass
class AnyDateTime:
    after: typing.Optional[typing.Union[datetime, date, time, timedelta]] = None
    before: typing.Optional[typing.Union[datetime, date, time, timedelta]] = None

    def __eq__(self, other):
        if not (isinstance(other, datetime) or isinstance(other, date) or isinstance(other, time)):
            return False
        if self.after:
            after = self._handle_timedelta(self.after)
            coerced_other, after = self._coerce_types(other, after)
            if not coerced_other > after:
                return False
        if self.before:
            before = self._handle_timedelta(self.before)
            coerced_other, before = self._coerce_types(other, before)
            if not coerced_other < before:
                return False
        return True

    @staticmethod
    def _handle_timedelta(
            bound: typing.Union[datetime, date, time, timedelta]
    ) -> typing.Union[datetime, date, time]:
        """When timedelta is passed, it is used as a relative time compared when
        the assertion is executed."""
        if type(bound) == timedelta:
            return datetime.now() + bound
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


# before=timedelta(milliseconds=1) to allow current time
LAST_SECOND = AnyDateTime(after=timedelta(seconds=-1), before=timedelta(milliseconds=1))
LAST_MINUTE = AnyDateTime(after=timedelta(minutes=-1), before=timedelta(milliseconds=1))
LAST_HOUR = AnyDateTime(after=timedelta(hours=-1), before=timedelta(milliseconds=1))
LAST_DAY = AnyDateTime(after=timedelta(days=-1), before=timedelta(milliseconds=1))
LAST_WEEK = AnyDateTime(after=timedelta(weeks=-1), before=timedelta(milliseconds=1))
LAST_YEAR = AnyDateTime(after=timedelta(days=-365), before=timedelta(milliseconds=1))

# TODO:
# THIS_MINUTE
# THIS_HOUR
THIS_DAY = AnyDateTime(
    after=date.today() - timedelta(days=1), before=date.today() + timedelta(days=1)
)
TODAY = THIS_DAY
# THIS_DAY / TODAY
# THIS_WEEK
# THIS_MONTH
# THIS_YEAR

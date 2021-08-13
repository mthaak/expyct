import typing
from dataclasses import dataclass
from datetime import datetime, date, time, timedelta, timezone

from expyct.base import Equals, MapBefore, Predicate

T = typing.TypeVar("T")


@dataclass
class AfterBefore(typing.Generic[T]):
    """Mixin for matching a `date`, `time`, or `datetime` that takes place after, before, or on
    given date/time. In other words, it is inclusive on both sides.

    Arguments:
        after : object must occur after or exactly on given
        before : object must occur before or exactly on given
    """

    after: typing.Optional[T] = None
    before: typing.Optional[T] = None

    def __eq__(self, other):
        if self.after is not None and not other >= self.after:
            return False
        if self.before is not None and not other <= self.before:
            return False
        return True


@dataclass
class AfterBeforeStrict(typing.Generic[T]):
    """Mixin for matching a `date`, `time`, or `datetime` that takes place after and/or before given
    date/time. In other words, it is exclusive on both sides.

    Arguments:
        after_strict : object must occur after given
        before_strict : object must occur before given
    """

    after_strict: typing.Optional[T] = None
    before_strict: typing.Optional[T] = None

    def __eq__(self, other):
        if self.after_strict is not None and not other > self.after_strict:
            return False
        if self.before_strict is not None and not other < self.before_strict:
            return False
        return True


@dataclass
class DateTime(
    MapBefore, Equals[datetime], AfterBefore[datetime], AfterBeforeStrict[datetime], Predicate
):
    """Match any object that is an instance of `datetime`.

    Arguments:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        after : object must occur after or exactly on given
        before : object must occur before or exactly on given
        after_strict : object must occur after given
        before_strict : object must occur before given
        pred : object must satisfy predicate
    """

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
        if not AfterBeforeStrict.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


@dataclass
class DateTimeTz(
    MapBefore, Equals[datetime], AfterBefore[datetime], AfterBeforeStrict[datetime], Predicate
):
    """Match any object that is an instance of `datetime` and has timezone information (`tzinfo`).
    In other words, is a timestamp.

    Arguments:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        after : object must occur after or on given. If timedelta is given, then it is compared
            relative to when the assertion is run
        before : object must occur before or on given. If timedelta is given, then it is compared
            relative to when the assertion is run
        after_strict : object must occur after given
        before_strict : object must occur before given
        pred : object must satisfy predicate
    """

    after: typing.Optional[typing.Union[datetime, timedelta]] = None  # type: ignore
    before: typing.Optional[typing.Union[datetime, timedelta]] = None  # type: ignore
    after_strict: typing.Optional[typing.Union[datetime, timedelta]] = None  # type: ignore
    before_strict: typing.Optional[typing.Union[datetime, timedelta]] = None  # type: ignore

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not type(other) == datetime:
            return False
        if other.tzinfo is None:
            return False
        if self.equals:
            if self.equals.tzinfo is None:
                raise ValueError("equals is missing tzinfo")
        if not Equals.__eq__(self, other):
            return False
        if self.before:
            self.before = DateTimeTz._handle_timedelta(self.before)
            if self.before.tzinfo is None:
                raise ValueError("before is missing tzinfo")
        if self.after:
            self.after = DateTimeTz._handle_timedelta(self.after)
            if self.after.tzinfo is None:
                raise ValueError("after is missing tzinfo")
        if not AfterBefore.__eq__(self, other):
            return False
        if self.before_strict:
            self.before_strict = DateTimeTz._handle_timedelta(self.before_strict)
            if self.before_strict.tzinfo is None:
                raise ValueError("before_strict is missing tzinfo")
        if self.after_strict:
            self.after_strict = DateTimeTz._handle_timedelta(self.after_strict)
            if self.after_strict.tzinfo is None:
                raise ValueError("after_strict is missing tzinfo")
        if not AfterBeforeStrict.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True

    @staticmethod
    def _handle_timedelta(
        bound: typing.Union[datetime, date, time, timedelta]
    ) -> typing.Union[datetime, date, time]:
        """When timedelta is passed, it is used as a time relative to when the assertion is
        executed."""

        if isinstance(bound, timedelta):
            return datetime.now().astimezone(timezone.utc) + bound
        else:
            return bound


@dataclass
class Date(MapBefore, Equals[date], AfterBefore[date], AfterBeforeStrict[date], Predicate):
    """Match any object that is an instance of `date`.

    Arguments:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        after : object must occur after or exactly on given
        before : object must occur before or exactly on given
        after_strict : object must occur after given
        before_strict : object must occur before given
        pred : object must satisfy predicate
    """

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
        if not AfterBeforeStrict.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


@dataclass
class Time(MapBefore, Equals[time], AfterBefore[time], AfterBeforeStrict[time], Predicate):
    """Match any object that is an instance of `time`.

    Arguments:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        after : object must occur after or exactly on given
        before : object must occur before or exactly on given
        after_strict : object must occur after given
        before_strict : object must occur before given
        pred : object must satisfy predicate
    """

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
        if not AfterBeforeStrict.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


def parse_isoformat(dt: str) -> typing.Union[date, time, datetime]:
    """Parse a ISO8601-formatted string as a `date`, `datetime` or `datetime` object.

        This will depend on the amount of information that is given.

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
                if dt.endswith("Z"):
                    dt = dt[:-1] + "+00:00"
                return datetime.fromisoformat(dt).astimezone(timezone.utc)
    raise ValueError("Only str is allowed as input")


#: Any instance of `datetime`
ANY_DATETIME = DateTime()
#: Any instance of `date`
ANY_DATE = Date()
#: Any instance `time`
ANY_TIME = Time()

#: Any string that can be parsed as `datetime` using the ISO8601 format
ANY_DATETIME_ISO = DateTime(map_before=parse_isoformat)
#: Any string that can be parsed as `date` using the ISO8601 format
ANY_DATE_ISO = Date(map_before=parse_isoformat)
#: Any string that can be parsed as `time` using the ISO8601 format
ANY_TIME_ISO = Time(map_before=parse_isoformat)

#: Any timestamp occurring during the last second
LAST_SECOND = DateTimeTz(after=timedelta(seconds=-1), before=timedelta())
#: Any timestamp occurring during the last 60 seconds
LAST_MINUTE = DateTimeTz(after=timedelta(minutes=-1), before=timedelta())
#: Any timestamp occurring during the last 60 minutes
LAST_HOUR = DateTimeTz(after=timedelta(hours=-1), before=timedelta())
#: Any timestamp occurring during the last 24 hours
LAST_DAY = DateTimeTz(after=timedelta(days=-1), before=timedelta())
#: Any timestamp occurring during the last 7 days
LAST_WEEK = DateTimeTz(after=timedelta(weeks=-1), before=timedelta())
#: Any timestamp occurring during the last 365 days
LAST_YEAR = DateTimeTz(after=timedelta(days=-365), before=timedelta())
#: Any timestamp occurring during the last second, parsed from ISO8601 string
LAST_SECOND_ISO = DateTimeTz(
    after=timedelta(seconds=-1), before=timedelta(), map_before=parse_isoformat
)
#: Any timestamp occurring during the last 60 seconds, parsed from ISO8601 string
LAST_MINUTE_ISO = DateTimeTz(
    after=timedelta(minutes=-1), before=timedelta(), map_before=parse_isoformat
)
#: Any timestamp occurring during the last 60 minutes, parsed from ISO8601 string
LAST_HOUR_ISO = DateTimeTz(
    after=timedelta(hours=-1), before=timedelta(), map_before=parse_isoformat
)
#: Any timestamp occurring during the last 24 hours, parsed from ISO8601 string
LAST_DAY_ISO = DateTimeTz(after=timedelta(days=-1), before=timedelta(), map_before=parse_isoformat)
#: Any timestamp occurring during the last 7 days, parsed from ISO8601 string
LAST_WEEK_ISO = DateTimeTz(
    after=timedelta(weeks=-1), before=timedelta(), map_before=parse_isoformat
)
#: Any timestamp occurring during the last 365 days, parsed from ISO8601 string
LAST_YEAR_ISO = DateTimeTz(
    after=timedelta(days=-365), before=timedelta(), map_before=parse_isoformat
)


def floor_second(dt: datetime):
    return dt.replace(microsecond=0)


def floor_minute(dt: datetime):
    return dt.replace(second=0, microsecond=0)


def floor_hour(dt: datetime):
    return dt.replace(minute=0, second=0, microsecond=0)


def floor_day(dt: datetime):
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def floor_year(dt: datetime):
    return dt.replace(month=0, day=0, hour=0, minute=0, second=0, microsecond=0)


#: Any timestamp occurring in the current second
THIS_SECOND = DateTimeTz(
    after_strict=floor_second(datetime.now()) - timedelta(seconds=1),
    before_strict=floor_second(datetime.now()) + timedelta(seconds=1),
)
#: Any timestamp occurring in the current minute
THIS_MINUTE = DateTimeTz(
    after_strict=floor_minute(datetime.now()) - timedelta(minutes=1),
    before_strict=floor_minute(datetime.now()) + timedelta(minutes=1),
)
#: Any timestamp occurring in the current hour
THIS_HOUR = DateTimeTz(
    after_strict=floor_hour(datetime.now()) - timedelta(hours=1),
    before_strict=floor_hour(datetime.now()) + timedelta(hours=1),
)
#: Any timestamp occurring on the current day
THIS_DAY = DateTimeTz(
    after_strict=floor_day(datetime.now()) - timedelta(days=1),
    before_strict=floor_day(datetime.now()) + timedelta(days=1),
)
#: The same as THIS_DAY
TODAY = THIS_DAY

#: Any timestamp occurring on the current day, parsed from ISO8601 string
THIS_DAY_ISO = DateTimeTz(
    after_strict=floor_day(datetime.now()) - timedelta(days=1),
    before_strict=floor_day(datetime.now()) + timedelta(days=1),
    map_before=parse_isoformat,
)
#: The same as THIS_DAY_ISO
TODAY_ISO = THIS_DAY_ISO

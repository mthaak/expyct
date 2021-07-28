import typing
from dataclasses import dataclass
from datetime import datetime, date, time, timedelta


@dataclass
class BeforeAfter:
    after: typing.Optional[typing.Union[datetime, date, time]] = None
    before: typing.Optional[typing.Union[datetime, date, time]] = None

    def __eq__(self, other):
        if self.after and not other > self.after:
            return False
        if self.before and not other < self.before:
            return False
        return True


@dataclass
class DateTime(BeforeAfter):

    def __eq__(self, other):
        if not isinstance(other, datetime):
            return False
        if not BeforeAfter.__eq__(self, other):
            return False
        return True


@dataclass
class Date(BeforeAfter):

    def __eq__(self, other):
        if not isinstance(other, date):
            return False
        if not BeforeAfter.__eq__(self, other):
            return False
        return True


@dataclass
class Time(BeforeAfter):

    def __eq__(self, other):
        if not isinstance(other, time):
            return False
        if not BeforeAfter.__eq__(self, other):
            return False
        return True


LAST_DAY = BeforeAfter(after=datetime.now() - timedelta(days=1), before=datetime.now())
LAST_WEEK = BeforeAfter(after=datetime.now() - timedelta(weeks=1), before=datetime.now())
LAST_YEAR = BeforeAfter(after=datetime.now() - timedelta(days=365), before=datetime.now())

# TODO:
# THIS_MINUTE
# THIS_HOUR
THIS_DAY = BeforeAfter(after=datetime.now().date() - timedelta(days=1),
                       before=datetime.now().date() + timedelta(days=1))
TODAY = THIS_DAY
# THIS_DAY / TODAY
# THIS_WEEK
# THIS_MONTH
# THIS_YEAR

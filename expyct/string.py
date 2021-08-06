import re
import typing
from dataclasses import dataclass

from expyct.base import Equals, MapBefore, Instance, Predicate
from expyct.collection import Length, Contains


@dataclass
class String(MapBefore, Equals[str], Instance, Length, Contains, Predicate):
    regex: typing.Optional[typing.Union[str, re.Pattern]] = None
    ignore_case: bool = False

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not (isinstance(other, str) or isinstance(other, bytes)):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Instance.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if not Contains.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        if self.regex:
            if isinstance(self.regex, str) and not re.fullmatch(
                self.regex, str(other), self.flags()
            ):
                return False
            if isinstance(self.regex, re.Pattern) and not self.regex.fullmatch(other):
                return False
        return True

    def flags(self):
        flags = 0
        if self.ignore_case:
            flags |= re.IGNORECASE
        return flags


ANY_UUID = String(
    regex=re.compile("[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12}")
)

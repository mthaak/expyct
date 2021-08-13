import re
import typing
from dataclasses import dataclass

from expyct.base import Equals, MapBefore, Instance, Predicate
from expyct.collection import Length, Contains


@dataclass
class String(MapBefore, Equals[str], Instance, Length, Contains, Predicate):
    """Match any object that is a string.

    Arguments:
          map_before : apply function before checking equality
          type : type of object must equal to given type
          instance_of : object must be an instance of given type
          equals : object must equal exactly. This is useful together with
              `map_before` to check a value after applying a function
          length : object length must be exactly
          min_length : object length must be at least
          max_length : object length must be at most
          non_empty : object must have at least one member
          superset_of : collection of which the object must be a superset
          subset_of : collection of which the object must be a subset
          pred : object must satisfy predicate
          regex : string must fully mach predicate
          ignore_case : whether to ignore case for equality and regex matching
    """

    regex: typing.Optional[typing.Union[str, re.Pattern]] = None
    ignore_case: bool = False

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if self.ignore_case:
            other = other.lower()
            if self.equals is not None:
                self.equals = self.equals.lower()
        if not isinstance(other, (str, bytes)):
            return False
        if not Instance.__eq__(self, other):
            return False
        if not Equals.__eq__(self, other):
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


#: Any string in the form of a UUID
ANY_UUID = String(
    regex=re.compile("[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12}")
)

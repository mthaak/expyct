import re
import typing
from dataclasses import dataclass

from expyct.base import Equals, MapBefore, Instance, Satisfies, Optional
from expyct.collection import Length, Contains


@dataclass
class String(
    Satisfies,
    Contains,
    Length,
    Equals[str],
    Instance,
    Optional,
    MapBefore,
):
    """Match any object that is a string.

    Arguments:
          map_before : apply function before checking equality
          optional : whether `None` is allowed
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
          satisfies : object must satisfy predicate
          starts_with : string must start with given
          ends_with : string must end with given
          regex : string must fully match predicate
          ignore_case : whether to ignore case for starts_with, ends_with,
            equality and regex matching
    """

    starts_with: typing.Optional[str] = None
    ends_with: typing.Optional[str] = None
    regex: typing.Optional[typing.Union[str, bytes, typing.Pattern]] = None
    ignore_case: bool = False

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if other is None:
            return Optional.__eq__(self, other)
        if self.ignore_case:
            other = other.lower()
            if self.equals is not None:
                self.equals = self.equals.lower()
            if self.starts_with is not None:
                self.starts_with = self.starts_with.lower()
            if self.ends_with is not None:
                self.ends_with = self.ends_with.lower()
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
        if not Satisfies.__eq__(self, other):
            return False
        if self.starts_with is not None:
            if not other.startswith(self.starts_with):
                return False
        if self.ends_with is not None:
            if not other.endswith(self.ends_with):
                return False
        if self.regex:
            if isinstance(self.regex, (str, bytes)) and not re.fullmatch(
                self.regex, str(other), self.flags()
            ):
                return False
            if isinstance(self.regex, typing.Pattern) and not self.regex.fullmatch(other):
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

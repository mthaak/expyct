import typing
from dataclasses import dataclass

from expyct.base import Equals, MapBefore, Predicate
from expyct.base import Instance


@dataclass
class Length:
    """Constrain by object len().

    Attributes:
        length : Object length must be exactly
        min_length : Object length must be at least
        max_length : Object length must be at most
        non_empty : Object must have at least one member
    """

    # blabla
    length: typing.Optional[int] = None
    min_length: typing.Optional[int] = None
    max_length: typing.Optional[int] = None
    non_empty: bool = False

    def __eq__(self, other):
        if self.length is not None and not len(other) == self.length:
            return False
        if self.min_length is not None and not len(other) >= self.min_length:
            return False
        if self.max_length is not None and not len(other) <= self.max_length:
            return False
        if self.non_empty and not len(other) > 0:
            return False
        return True


@dataclass
class Contains:
    subset_of: typing.Optional[typing.Collection] = None
    superset_of: typing.Optional[typing.Collection] = None

    def __eq__(self, other):
        if self.subset_of is not None:
            if isinstance(other, dict) and isinstance(self.subset_of, dict):
                if not all(x in self.subset_of.items() for x in other.items()):
                    return False
            else:
                if not all(x in self.subset_of for x in other):
                    return False

        if self.superset_of is not None:
            if isinstance(other, dict) and isinstance(self.superset_of, dict):
                if not all(x in other.items() for x in self.superset_of.items()):
                    return False
            else:
                if not all(x in other for x in self.superset_of):
                    return False
        return True


@dataclass
class Collection(MapBefore, Equals[typing.Collection], Instance, Length, Contains, Predicate):
    """Any instance of `Collection`."""

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not isinstance(other, typing.Collection):
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
        return True


@dataclass
class List(MapBefore, Equals[list], Length, Contains, Predicate):
    """Any instance of `list`."""

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not isinstance(other, list):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if not Contains.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


@dataclass
class Tuple(MapBefore, Equals[tuple], Length, Contains, Predicate):
    """Any instance of `tuple`."""

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not isinstance(other, tuple):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if not Contains.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


@dataclass
class Set(MapBefore, Equals[set], Length, Contains, Predicate):
    """Any instance of `set`."""

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not isinstance(other, set):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if not Contains.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True


@dataclass
class Dict(MapBefore, Equals[dict], Length, Contains, Predicate):
    """Any instance of `dict`."""

    keys: typing.Optional[typing.Any] = None
    values: typing.Optional[typing.Any] = None
    subset_of: typing.Optional[dict] = None
    superset_of: typing.Optional[dict] = None

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not isinstance(other, dict):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Length.__eq__(self, other):
            return False
        if self.keys is not None and not other.keys() == self.keys:
            return False
        if self.values is not None and not other.values() == self.values:
            return False
        if not Contains.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        return True

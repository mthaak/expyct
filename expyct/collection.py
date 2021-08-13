import typing
from dataclasses import dataclass

from expyct.base import Equals, MapBefore, Predicate
from expyct.base import Instance


@dataclass
class Length:
    """Match a collection object by its length as the result of len().

    Attributes:
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
    """

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
    """Match a collection object by the containment of specified members.

    Attributes:
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
    """

    superset_of: typing.Optional[typing.Collection] = None
    subset_of: typing.Optional[typing.Collection] = None

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
    """Match any object that is an instance of `Collection`.

    Attributes:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        type : type of object must equal to given type
        instance_of : object must be an instance of given type
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        pred : object must satisfy predicate
    """

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
    """Match any object that is an instance of `list`.

    Attributes:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        pred : object must satisfy predicate
    """

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
    """Match any object that is an instance of `tuple`.

    Attributes:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        pred : object must satisfy predicate
    """

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
    """Match any object that is an instance of `set`.

    Attributes:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        pred : object must satisfy predicate
    """

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
    """Match any object that is an instance of `dict`.

    Attributes:
        map_before : apply function before checking equality
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        length : object length must be exactly
        min_length : object length must be at least
        max_length : object length must be at most
        non_empty : object must have at least one member
        keys : object keys must equal
        values : object values must equal
        superset_of : collection of which the object must be a superset
        subset_of : collection of which the object must be a subset
        pred : object must satisfy predicate
    """

    keys: typing.Optional[typing.Set] = None
    values: typing.Optional[typing.List] = None
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

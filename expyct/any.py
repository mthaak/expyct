import typing
from dataclasses import dataclass

from expyct.base import MapBefore, Satisfies, Instance, Type, Equals, Vars, Optional


@dataclass
class Any(Satisfies, Vars, Equals[typing.Any], Optional, MapBefore):
    """Match any object.

    Attributes:
        map_before : apply function before checking equality
        optional : whether `None` is allowed
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        vars : object attributes (result of `vars()`) must equal
        satisfies : object must satisfy predicate
    """

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if other is None:
            return Optional.__eq__(self, other)
        if not Equals.__eq__(self, other):
            return False
        if not Vars.__eq__(self, other):
            return False
        if not Satisfies.__eq__(self, other):
            return False
        return True


@dataclass
class AnyValue(Instance, Satisfies, Vars, Equals[typing.Any], Optional, MapBefore):
    """Match any value.

    Attributes:
        map_before : apply function before checking equality
        optional : whether `None` is allowed
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        vars : object attributes (result of `vars()`) must equal
        satisfies : object must satisfy predicate
        type : type of object must equal to given type
        instance_of : object must be an instance of given type
    """

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if other is None:
            return Optional.__eq__(self, other)
        if not Equals.__eq__(self, other):
            return False
        if not Vars.__eq__(self, other):
            return False
        if not Satisfies.__eq__(self, other):
            return False
        if not Instance.__eq__(self, other):
            return False
        return True


@dataclass
class AnyType(Type, Satisfies, Vars, Equals[typing.Any], Optional, MapBefore):
    """Match any class.

    Attributes:
        map_before : apply function before checking equality
        optional : whether `None` is allowed
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        vars : object attributes (result of `vars()`) must equal
        satisfies : object must satisfy predicate
        superclass_of : class must be superclass of given type
        subclass_of : class must be subclass of given type
    """

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if other is None:
            return Optional.__eq__(self, other)
        if not Equals.__eq__(self, other):
            return False
        if not Vars.__eq__(self, other):
            return False
        if not Satisfies.__eq__(self, other):
            return False
        if not Type.__eq__(self, other):
            return False
        return True


#: Literally anything
ANY = Any()
#: Any value
ANY_VALUE = AnyValue()
#: Any type (i.e. class)
ANY_TYPE = AnyType()

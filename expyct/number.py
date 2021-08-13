import typing
from dataclasses import dataclass
from numbers import Number as ParentNumber

from expyct.base import MapBefore, Predicate, Equals, Instance


@dataclass
class MinMax:
    """Mixin for matching a number that is equal to, larger or smaller than given bounds.

    Arguments:
        min : number must be larger than or equal to given
        max : number must be smaller than or equal to given
    """

    min: typing.Optional[ParentNumber] = None  # TODO better type?
    max: typing.Optional[ParentNumber] = None

    def __eq__(self, other):
        if self.min is not None and not other >= self.min:
            return False
        if self.max is not None and not other <= self.max:
            return False
        return True


@dataclass
class MinMaxStrict:
    """Mixin for matching number that is strictly larger or smaller than given bounds.

    Arguments:
        min_strict : number must be larger than given
        max_strict : number must be smaller than given
    """

    min_strict: typing.Optional[ParentNumber] = None
    max_strict: typing.Optional[ParentNumber] = None

    def __eq__(self, other):
        if self.min_strict is not None and not other > self.min_strict:
            return False
        if self.max_strict is not None and not other < self.max_strict:
            return False
        return True


@dataclass
class CloseTo:
    """Mixin for matching number that is close to given target within a certain two-side error. In
    other words, the difference between the number and `close_to` must be at most `error`.

    Arguments:
        close_to : number must be close to this
        error : two-sided allowed error
    """

    close_to: typing.Optional[ParentNumber] = None
    error: float = 0.001

    def __eq__(self, other):
        if self.close_to is not None:
            d = self.error * self.close_to
            if not self.close_to - d <= other <= self.close_to + d:
                return False
        return True


@dataclass
class Number(MapBefore, Instance, Equals[ParentNumber], Predicate, MinMax, MinMaxStrict, CloseTo):
    """Match any number.

    Arguments:
        map_before : apply function before checking equality
        type : type of object must equal to given type
        instance_of : object must be an instance of given type
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        pred : object must satisfy predicate
        min : number must be larger than or equal to given
        max : number must be smaller than or equal to given
        min_strict : number must be larger than given
        max_strict : number must be smaller than given
        close_to : number must be close to this
        error : two-sided allowed error
    """

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not isinstance(other, ParentNumber):
            return False
        if not Instance.__eq__(self, other):
            return False
        if not Equals.__eq__(self, other):
            return False
        if not Predicate.__eq__(self, other):
            return False
        if not MinMax.__eq__(self, other):
            return False
        if not MinMaxStrict.__eq__(self, other):
            return False
        if not CloseTo.__eq__(self, other):
            return False
        return True


@dataclass
class Int(Number):
    """Match any object that is an instance of `int`.

    Arguments:
        map_before : apply function before checking equality
        type : type of object must equal to given type
        instance_of : object must be an instance of given type
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        pred : object must satisfy predicate
        min : number must be larger than or equal to given
        max : number must be smaller than or equal to given
        min_strict : number must be larger than given
        max_strict : number must be smaller than given
        close_to : number must be close to this
        error : two-sided allowed error
    """

    def __eq__(self, other):
        if not isinstance(other, int):
            return False
        if not Number.__eq__(self, other):
            return False
        return True


@dataclass
class Float(Number):
    """Match any object that is an instance of `float`.

    Arguments:
        map_before : apply function before checking equality
        type : type of object must equal to given type
        instance_of : object must be an instance of given type
        equals : object must equal exactly. This is useful together with
            `map_before` to check a value after applying a function
        pred : object must satisfy predicate
        min : number must be larger than or equal to given
        max : number must be smaller than or equal to given
        min_strict : number must be larger than given
        max_strict : number must be smaller than given
        close_to : number must be close to this
        error : two-sided allowed error
    """

    def __eq__(self, other):
        if not isinstance(other, float):
            return False
        if not Number.__eq__(self, other):
            return False
        return True


def parse_number_string(obj: str) -> typing.Union[int, float]:
    """Parse a string as number. First tries to parse as `int`, then as `float`. Throws a ValueError
    if `obj` is not a string.

    Args:
        obj : the string to parse
    """
    if not isinstance(obj, str):
        raise ValueError()
    try:
        return int(obj)
    except ValueError:
        return float(obj)


def parse_int_string(obj: str) -> int:
    """Parse a string as `int`. Throws a ValueError if `obj` is not a string.

    Args:
        obj : the string to parse
    """
    if not isinstance(obj, str):
        raise ValueError()
    return int(obj)


def parse_float_string(obj: str) -> float:
    """Parse a string as `float`. Throws a ValueError if `obj` is not a string.

    Args:
        obj : the string to parse
    """
    if not isinstance(obj, str):
        raise ValueError()
    return float(obj)


#: Any number
ANY_NUMBER = Number()
#: Any instance of `int`
ANY_INT = Int()
#: Any instance of `float`
ANY_FLOAT = Float()

#: Any number, parsed from a string
ANY_NUMBER_STRING = Number(map_before=parse_number_string)
#: Any instance of `int`
ANY_INT_STRING = Int(map_before=parse_int_string)
#: Any instance of `float`
ANY_FLOAT_STRING = Float(map_before=parse_float_string)

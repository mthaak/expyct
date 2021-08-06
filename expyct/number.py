import typing
from dataclasses import dataclass
from numbers import Number as ParentNumber

from expyct.base import MapBefore, Predicate


@dataclass
class MinMax:
    """Constrain a number to be equal, larger or smaller than given bounds."""

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
    """Constrain a number to be strictly larger or smaller than given bounds."""

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
    """Constrain a number close to given target within a certain two-side error."""

    close_to: typing.Optional[ParentNumber] = None
    error: float = 0.001

    def __eq__(self, other):
        if self.close_to is not None:
            d = self.error * self.close_to
            if not self.close_to - d <= other <= self.close_to + d:
                return False
        return True


@dataclass
class Number(MapBefore, Predicate, MinMax, MinMaxStrict, CloseTo):
    """Any number object."""

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not isinstance(other, ParentNumber):
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
    """Any `int`."""

    def __eq__(self, other):
        if not isinstance(other, int):
            return False
        if not Number.__eq__(self, other):
            return False
        return True


@dataclass
class Float(Number):
    """Any `float`."""

    def __eq__(self, other):
        if not isinstance(other, float):
            return False
        if not Number.__eq__(self, other):
            return False
        return True


ANY_NUMBER = Number()
ANY_INT = Int()
ANY_FLOAT = Float()

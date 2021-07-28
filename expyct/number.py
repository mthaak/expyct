import typing
from dataclasses import dataclass
from numbers import Number as ParentNumber

from expyct.base import MapBefore, Pred


@dataclass
class MinMax:
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
    min_strict: typing.Optional[ParentNumber] = None
    max_strict: typing.Optional[ParentNumber] = None

    def __eq__(self, other):
        if self.min_strict is not None and not other > self.min_strict:
            return False
        if self.max_strict is not None and not other < self.max_strict:
            return False
        return True


@dataclass
class Number(MapBefore, Pred, MinMax, MinMaxStrict):
    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not isinstance(other, ParentNumber):
            return False
        if not Pred.__eq__(self, other):
            return False
        if not MinMax.__eq__(self, other):
            return False
        if not MinMaxStrict.__eq__(self, other):
            return False
        return True


@dataclass
class Int(Number):
    def __eq__(self, other):
        if not isinstance(other, int):
            return False
        if not Number.__eq__(self, other):
            return False
        return True


@dataclass
class Float(Number):
    def __eq__(self, other):
        if not isinstance(other, float):
            return False
        if not Number.__eq__(self, other):
            return False
        return True


NUMBER = Number()
INT = Int()
FLOAT = Float()

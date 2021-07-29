import typing
from dataclasses import dataclass
from numbers import Number as ParentNumber


@dataclass
class MapBefore:
    map_before: typing.Optional[typing.Callable] = None

    def map(self, other):
        if self.map_before:
            return self.map_before(other)
        else:
            return other


@dataclass
class Pred:
    pred: typing.Optional[typing.Callable[[], bool]] = None

    def __eq__(self, other):
        if self.pred:
            try:
                return self.pred(other)
            except Exception:
                return False
        return True


@dataclass
class Instance:
    type: typing.Optional[typing.Type] = None
    instanceof: typing.Optional[typing.Type] = None

    def __eq__(self, other):
        # TODO check
        if not (isinstance(other, ParentNumber) or isinstance(other, typing.Collection)):
            return False
        if self.type and type(other) != self.type:
            return False
        if self.instanceof and not isinstance(other, self.instanceof):
            return False
        return True


@dataclass
class Class:
    type: typing.Optional[typing.Type] = None
    subclassof: typing.Optional[typing.Type] = None

    def __eq__(self, other):
        if not type(other) == type:
            return False
        if self.type and other != self.type:
            return False
        if self.subclassof and not issubclass(other, self.subclassof):
            return False
        return True

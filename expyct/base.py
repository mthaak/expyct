from dataclasses import dataclass
from numbers import Number as ParentNumber
from typing import Callable, Optional, Type, Collection


# TODO use in other objects

@dataclass
class MapBefore:
    map_before: Optional[Callable] = None

    def map(self, other):
        if self.map_before:
            return self.map_before(other)
        else:
            return other


@dataclass
class Pred:
    pred: Optional[Callable[[], bool]] = None

    def __eq__(self, other):
        if self.pred:
            try:
                return self.pred(other)
            except Exception:
                return False
        return True


@dataclass
class Instance:
    type: Optional[Type] = None
    instanceof: Optional[Type] = None

    def __eq__(self, other):
        if not (isinstance(other, ParentNumber) or isinstance(other, Collection)):  # TODO check
            return False
        if self.type and type(other) != self.type:
            return False
        if self.instanceof and not isinstance(other, self.instanceof):
            return False
        return True


@dataclass
class Type:
    type: Optional[Type] = None
    subclassof: Optional[Type] = None

    def __eq__(self, other):
        if not type(other) == type:
            return False
        if self.type and other != self.type:
            return False
        if self.subclassof and not issubclass(other, self.subclassof):
            return False
        return True

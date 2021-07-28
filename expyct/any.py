from dataclasses import dataclass

from expyct.base import MapBefore, Pred, Instance, Type


@dataclass
class Any(MapBefore, Pred):

    def __eq__(self, other):
        try:
            other = MapBefore.map(self, other)
        except Exception:
            return False
        if not Pred.__eq__(self, other):
            return False
        return True


@dataclass
class AnyValue(Any, Instance):

    def __eq__(self, other):
        if not Any.__eq__(self, other):
            return False
        if not Instance.__eq__(self, other):
            return False
        return True


@dataclass
class AnyType(Any, Type):

    def __eq__(self, other):
        if not Any.__eq__(self, other):
            return False
        if not Type.__eq__(self, other):
            return False
        return True

ANY = Any()
ANYVALUE = AnyValue()
ANYTYPE = AnyType()

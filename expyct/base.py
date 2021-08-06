import abc
import inspect
import typing
from dataclasses import dataclass

T = typing.TypeVar("T")


@dataclass
class MapBefore:
    map_before: typing.Optional[typing.Callable] = None

    def map(self, other):
        if self.map_before:
            return self.map_before(other)
        else:
            return other


@dataclass
class Predicate:
    pred: typing.Optional[typing.Callable[[], bool]] = None

    def __eq__(self, other):
        if self.pred:
            try:
                return self.pred(other)
            except Exception:
                return False
        return True


@dataclass
class Equals(typing.Generic[T]):
    equals: typing.Optional[T] = None

    def __eq__(self, other):
        if self.equals is not None and not other == self.equals:
            return False
        return True


@dataclass
class Instance:
    """
    Match a class instance.

    Attributes:
        type : type of object must equal given type
        instance_of : object must be an instance of given type
    """

    type: typing.Optional[typing.Type] = None
    instance_of: typing.Optional[typing.Type] = None

    def __eq__(self, other):
        # TODO check
        if (
            inspect.ismodule(other)
            or inspect.isclass(other)
            or inspect.isfunction(other)
            or inspect.ismethod(other)
        ):
            return False
        if self.type and type(other) != self.type:
            return False
        if self.instance_of and not isinstance(other, self.instance_of):
            return False
        return True


@dataclass
class Type:
    """
    Match a type.

    Attributes:
        superclass_of : class must be superclass of given type
        subclass_of : class must be subclass of given type
    """

    superclass_of: typing.Optional[typing.Type] = None
    subclass_of: typing.Optional[typing.Type] = None

    def __eq__(self, other):
        if not (type(other) == type or type(other) == abc.ABCMeta):
            return False
        if self.superclass_of and not issubclass(self.superclass_of, other):
            return False
        if self.subclass_of and not issubclass(other, self.subclass_of):
            return False
        return True

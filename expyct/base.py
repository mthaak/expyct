import abc
import inspect
import typing
from dataclasses import dataclass

T = typing.TypeVar("T")


@dataclass
class MapBefore:
    """Mixing for applying a function before checking equality."""

    def __init__(self, map_before: typing.Optional[typing.Callable] = None):
        """Mixing for applying a function before checking equality.

        Args:
            map_before : the mapping function to apply
        """
        self.map_before = map_before

    map_before: typing.Optional[typing.Callable] = None

    def map(self, other):
        if self.map_before:
            return self.map_before(other)
        else:
            return other


@dataclass
class Satisfies:
    """Mixin for checking equality by using a predicate function.

    If `satisfies(obj)` returns `True`, then it is equal.
    """

    satisfies: typing.Optional[typing.Callable[[typing.Any], bool]] = None

    def __init__(self, satisfies: typing.Optional[typing.Callable[[typing.Any], bool]] = None):
        """Mixin for checking equality by using a predicate function.

        Args:
            satisfies : object must satisfy predicate
        """
        self.satisfies = satisfies

    def __eq__(self, other):
        if self.satisfies:
            try:
                return self.satisfies(other)
            except Exception:
                return False
        return True


@dataclass
class Equals(typing.Generic[T]):
    """Mixin for checking equality using a specific object to compare against."""

    equals: typing.Optional[T] = None

    def __init__(self, equals: typing.Optional[T] = None):
        """Mixin for checking equality using a specific object to compare against.

        Args:
            equals : the object to check equality with
        """
        self.equals = equals

    def __eq__(self, other):
        if self.equals is not None:
            if not other == self.equals:
                return False
        return True


@dataclass
class Vars:
    """Mixin for checking the presence of specific object attributes.

    The attributes are compared as a dict. So anything that can be compared
    with a dict can be used as `vars` argument, including other expyct objects like `expyct.Dict`.
    """

    vars: typing.Optional[typing.Any] = None

    def __init__(self, vars: typing.Optional[typing.Any] = None):
        """Mixin for checking the presence of specific object attributes.

        Args:
            vars : object attributes (result of `vars()`) must equal
        """
        self.vars = vars

    def __eq__(self, other):
        if self.vars is not None:
            if not vars(other) == self.vars:
                return False
        return True


@dataclass
class Optional:
    """Mixin for matching with `None`."""

    optional: typing.Optional[bool] = None

    def __init__(self, optional: typing.Optional[bool] = None):
        """Mixin for matching with `None`.

        Args:
            optional : whether `None` is allowed [default: `False`]
        """
        self.optional = optional

    def __eq__(self, other):
        if other is None:
            if self.optional is not None:
                return self.optional is True
            else:
                return False
        return True


@dataclass
class Instance:
    """Match any object that is a class instance."""

    type: typing.Optional[typing.Type] = None
    instance_of: typing.Optional[typing.Type] = None

    def __init__(
        self,
        type: typing.Optional[typing.Type] = None,
        instance_of: typing.Optional[typing.Type] = None,
    ):
        """Match any object that is a class instance.

        Args:
            type : type of object must equal to given type
            instance_of : object must be an instance of given type
        """
        self.type = type
        self.instance_of = instance_of

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
    """Match any object that is a type."""

    superclass_of: typing.Optional[typing.Type] = None
    subclass_of: typing.Optional[typing.Type] = None

    def __init__(
        self,
        superclass_of: typing.Optional[typing.Type] = None,
        subclass_of: typing.Optional[typing.Type] = None,
    ):
        """Match any object that is a type.

        Args:
            superclass_of : the type of which the matched object must be a superclass
            subclass_of : the type of which the matched object must be a subclass
        """
        self.superclass_of = superclass_of
        self.subclass_of = subclass_of

    def __eq__(self, other):
        if not (type(other) == type or type(other) == abc.ABCMeta):
            return False
        if self.superclass_of and not issubclass(self.superclass_of, other):
            return False
        if self.subclass_of and not issubclass(other, self.subclass_of):
            return False
        return True

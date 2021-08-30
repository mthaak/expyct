import typing
from copy import copy

T = typing.TypeVar("T")


def copy_update(obj: T, **updates) -> T:
    """Make a shallow copy of object and update specific attributes."""
    obj_copy = copy(obj)
    for k, v in updates.items():
        setattr(obj_copy, k, v)
    return obj_copy

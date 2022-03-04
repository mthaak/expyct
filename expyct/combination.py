import typing

from dataclasses import dataclass

from expyct.base import BaseMatcher


@dataclass(repr=False, eq=False)
class OneOf(BaseMatcher):
    """Object must equal one of the given options.

    This can be recursively used to check nested objects. For example:

    .. code-block:: python

        expyct.OneOf([
            expyct.ANY_DATE,
            expyct.dict(keys=["from", "until"], values=expyct.ANY_DATE)
        ])

    Args:
            options: objects to compare to
    """

    options: typing.Collection

    def __init__(self, options: typing.Collection):
        self.options = options

    def _eq(self, other):
        return any(option.__eq__(other) for option in self.options)

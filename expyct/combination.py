import typing
from dataclasses import dataclass


@dataclass
class OneOf:
    """Object must equal one of the given options.

    This can be recursively used to check nested objects. For example:

    .. code-block:: python

        expyct.OneOf([
            expyct.ANY_DATE,
            expyct.dict(keys=["from", "until"], values=expyct.ANY_DATE)
        ])
    """

    options: typing.Collection

    def __init__(self, options: typing.Collection):
        """Object must equal one of the given options.

        Args:
            options: objects to compare to
        """
        self.options = options

    def __eq__(self, other):
        return any(option.__eq__(other) for option in self.options)

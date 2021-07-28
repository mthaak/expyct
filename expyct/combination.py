import typing
from dataclasses import dataclass


@dataclass
class OneOf:
    options: typing.Collection

    def __eq__(self, other):
        return any(option.__eq__(other) for option in self.options)

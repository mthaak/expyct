import re
import typing
from dataclasses import dataclass


@dataclass
class String:
    regex: typing.Optional[typing.Union[str, re.Pattern]] = None
    ignore_case: bool = False

    def __eq__(self, other):
        if not (isinstance(other, str) or isinstance(other, bytes)):
            return False
        if self.regex:
            if isinstance(self.regex, str) and not re.fullmatch(
                self.regex, str(other), self.flags()
            ):
                return False
            if isinstance(self.regex, re.Pattern) and not self.regex.fullmatch(other):
                return False
        return True

    def flags(self):
        flags = 0
        if self.ignore_case:
            flags |= re.IGNORECASE
        return flags


UUID = String(
    regex=re.compile("[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12}")
)

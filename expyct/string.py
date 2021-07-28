import re
from dataclasses import dataclass
from typing import Union, Optional


@dataclass
class String:
    regex: Optional[Union[str, re.Pattern]] = None
    ignore_case: bool = False

    def __eq__(self, other):
        if not (isinstance(other, str) or isinstance(other, bytes)):
            return False
        if self.regex:
            if isinstance(self.regex, str) and not re.fullmatch(self.regex, str(other), self.flags()):
                return False
            if isinstance(self.regex, re.Pattern) and not self.regex.fullmatch(other):
                return False
        return True

    def flags(self):
        flags = 0
        if self.ignore_case:
            flags |= re.IGNORECASE
        return flags

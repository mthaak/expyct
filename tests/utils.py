import contextlib
import sys

import pytest

if sys.version_info < (3, 7):
    contextlib.nullcontext = contextlib.suppress


def raises_or_result(expect):
    if type(expect) == type and issubclass(expect, Exception):
        return pytest.raises(expect)
    return contextlib.nullcontext()

import contextlib

import pytest


def raises_or_result(expect):
    if type(expect) == type and issubclass(expect, Exception):
        return pytest.raises(expect)
    return contextlib.nullcontext()

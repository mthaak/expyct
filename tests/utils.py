import contextlib
import sys
from typing import ContextManager, Any

import pytest

if sys.version_info < (3, 7):
    contextlib.nullcontext = contextlib.suppress


def raises_or_result(expect: Any) -> ContextManager:
    """Returns a pytest.raises context manager only if `expect` is an exception, and returns
    a nullcontext otherwise."""
    if type(expect) == type and issubclass(expect, Exception):
        return pytest.raises(expect)
    return contextlib.nullcontext()

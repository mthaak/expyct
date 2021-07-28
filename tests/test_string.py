import re

import pytest as pytest

from expyct import String


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        ("abc", "abc", True),
        # test type
        ("abc", String(), True),
        (b"abc", String(), True),
        (1, String(), False),
        # test regex
        ("abc", String(regex="abc"), True),
        ("abc", String(regex="def"), False),
        ("abc", String(regex=r"abc"), True),
        ("abc", String(regex=r"def"), False),
        ("abc", String(regex=re.compile("abc")), True),
        ("abc", String(regex=re.compile("def")), False),
        ("abc", String(regex="ABC"), False),
        ("abc", String(regex="ABC", ignore_case=True), True),
        ("abc", String(regex=re.compile("ABC")), False),
        ("abc", String(regex=re.compile("ABC", re.IGNORECASE)), True),
    ],
)
def test_string(value, expect, result):
    assert (value == expect) == result

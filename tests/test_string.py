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
        ("abc", String(regex="abcd?"), True),
        ("abc", String(regex="defG?"), False),
        ("abc", String(regex=r"abcd?"), True),
        ("abc", String(regex=r"defg?"), False),
        ("abc", String(regex=re.compile("abcd?")), True),
        ("abc", String(regex=re.compile("defg?")), False),
        ("abc", String(regex="ABCD?"), False),
        ("abc", String(regex="ABCD?", ignore_case=True), True),
        ("abc", String(regex=re.compile("ABCD?")), False),
        ("abc", String(regex=re.compile("ABCD?", re.IGNORECASE)), True),
    ],
)
def test_string(value, expect, result):
    assert (value == expect) == result

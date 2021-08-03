import re

import pytest as pytest

import expyct as exp


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        ("abc", "abc", True),
        # test type
        ("abc", exp.String(), True),
        (b"abc", exp.String(), True),
        ([], exp.String(), False),
        (1, exp.String(), False),
        # test map before
        (1, exp.Collection(map_before=str), True),
        # test equals
        ("123", exp.Collection(equals="123"), True),
        ("123", exp.Collection(equals="12"), False),
        # test length
        ("123", exp.Collection(length=3), True),
        ("123", exp.Collection(length=2), False),
        # test min length
        ("12", exp.Collection(min_length=3), False),
        ("123", exp.Collection(min_length=3), True),
        ("1234", exp.Collection(min_length=3), True),
        # test max length
        ("12", exp.Collection(max_length=3), True),
        ("123", exp.Collection(max_length=3), True),
        ("1234", exp.Collection(max_length=3), False),
        # test non empty
        ("12", exp.Collection(non_empty=True), True),
        ([], exp.Collection(non_empty=True), False),
        # test subset of
        ("12", exp.Collection(subset_of="123"), True),
        ("124", exp.Collection(subset_of="123"), False),
        # test superset of
        ("123", exp.Collection(superset_of="12"), True),
        ("14", exp.Collection(superset_of="12"), False),
        # test predicate
        ("1234", exp.Collection(pred=lambda x: x.startswith("12")), True),
        ("1234", exp.Collection(pred=lambda x: len(x) == 10), False),
        # test regex
        ("abc", exp.String(regex="abcd?"), True),
        ("abc", exp.String(regex="defG?"), False),
        ("abc", exp.String(regex=r"abcd?"), True),
        ("abc", exp.String(regex=r"defg?"), False),
        ("abc", exp.String(regex=re.compile("abcd?")), True),
        ("abc", exp.String(regex=re.compile("defg?")), False),
        ("abc", exp.String(regex="ABCD?"), False),
        ("abc", exp.String(regex="ABCD?", ignore_case=True), True),
        ("abc", exp.String(regex=re.compile("ABCD?")), False),
        ("abc", exp.String(regex=re.compile("ABCD?", re.IGNORECASE)), True),
    ],
)
def test_string(value, expect, result):
    assert (value == expect) == result

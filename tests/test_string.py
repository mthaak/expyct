import re

import pytest as pytest

import expyct as exp


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        ("abc", "abc", True),
        # test type
        ([], exp.String(), False),
        (1, exp.String(), False),
        ("abc", exp.String(), True),
        (b"abc", exp.String(), True),
        # test map before
        (1, exp.String(map_before=str), True),
        # test optional
        (None, exp.String(), False),
        (None, exp.String(optional=True), True),
        # test equals
        ("123", exp.String(equals="12"), False),
        ("123", exp.String(equals="123"), True),
        # test length
        ("123", exp.String(length=2), False),
        ("123", exp.String(length=3), True),
        # test min length
        ("12", exp.String(min_length=3), False),
        ("123", exp.String(min_length=3), True),
        ("1234", exp.String(min_length=3), True),
        # test max length
        ("1234", exp.String(max_length=3), False),
        ("123", exp.String(max_length=3), True),
        ("12", exp.String(max_length=3), True),
        # test non empty
        ([], exp.String(non_empty=True), False),
        ("12", exp.String(non_empty=True), True),
        # test subset of
        ("124", exp.String(subset_of="123"), False),
        ("12", exp.String(subset_of="123"), True),
        # test superset of
        ("14", exp.String(superset_of="12"), False),
        ("123", exp.String(superset_of="12"), True),
        # test predicate
        ("1234", exp.String(satisfies=lambda x: len(x) == 10), False),
        ("1234", exp.String(satisfies=lambda x: x.startswith("12")), True),
        # test starts with
        ("abcd", exp.String(starts_with="cd"), False),
        ("abcd", exp.String(starts_with="ab"), True),
        ("abcd", exp.String(starts_with="AB", ignore_case=False), False),
        ("abcd", exp.String(starts_with="AB", ignore_case=True), True),
        ("ABCD", exp.String(starts_with="ab", ignore_case=True), True),
        # test ends with
        ("abcd", exp.String(ends_with="ab"), False),
        ("abcd", exp.String(ends_with="cd"), True),
        ("abcd", exp.String(ends_with="CD", ignore_case=False), False),
        ("abcd", exp.String(ends_with="CD", ignore_case=True), True),
        ("ABCD", exp.String(ends_with="cd", ignore_case=True), True),
        # test regex
        ("abc", exp.String(regex="defG?"), False),
        ("abc", exp.String(regex="abcd?"), True),
        ("abc", exp.String(regex=r"defg?"), False),
        ("abc", exp.String(regex=r"abcd?"), True),
        ("abc", exp.String(regex=re.compile("defg?")), False),
        ("abc", exp.String(regex=re.compile("abcd?")), True),
        ("abc", exp.String(regex="ABCD?"), False),
        ("abc", exp.String(regex="ABCD?", ignore_case=True), True),
        ("abc", exp.String(regex=re.compile("ABCD?")), False),
        ("abc", exp.String(regex=re.compile("ABCD?", re.IGNORECASE)), True),
    ],
)
def test_string(value, expect, result):
    assert (value == expect) == result

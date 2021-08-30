from typing import Collection

import pytest

import expyct as exp


class ABC:
    a = 1
    b = 2
    c = 3

    def __init__(self):
        self.x = 4
        self.y = 5
        self.z = 6


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (1, exp.Any(), True),
        ("abc", exp.Any(), True),
        ([], exp.Any(), True),
        (int, exp.Any(), True),
        (lambda x: x + 1, exp.Any(), True),
        # test map before and equals
        (1, exp.Any(equals=2), False),
        (1, exp.Any(equals=2, map_before=lambda x: x + 1), True),
        # test optional
        (None, exp.Any(), False),
        (None, exp.Any(optional=True), True),
        # test vars
        (ABC(), exp.Any(vars={"x": 4}), False),
        (ABC(), exp.Any(vars=exp.Dict(length=3)), True),
        # test predicate
        (1, exp.Any(satisfies=lambda x: x % 2 == 0), False),
        (2, exp.Any(satisfies=lambda x: x % 2 == 0), True),
    ],
)
def test_any(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (1, exp.AnyValue(), True),
        ("abc", exp.AnyValue(), True),
        ([], exp.AnyValue(), True),
        (int, exp.AnyValue(), False),
        (lambda x: x + 1, exp.AnyValue(), False),
        # test map before and equals
        (1, exp.AnyValue(equals=2), False),
        (1, exp.AnyValue(equals=2, map_before=lambda x: x + 1), True),
        # test optional
        (None, exp.AnyValue(), False),
        (None, exp.AnyValue(optional=True), True),
        # test vars
        (ABC(), exp.AnyValue(vars={"x": 4}), False),
        (ABC(), exp.AnyValue(vars=exp.Dict(length=3)), True),
        # test predicate
        (1, exp.AnyValue(satisfies=lambda x: x % 2 == 0), False),
        (2, exp.AnyValue(satisfies=lambda x: x % 2 == 0), True),
    ],
)
def test_any_value(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (1, exp.AnyType(), False),
        ("abc", exp.AnyType(), False),
        ([], exp.AnyType(), False),
        (int, exp.AnyType(), True),
        (lambda x: x + 1, exp.AnyType(), False),
        # test map before and equals
        (int, exp.AnyType(equals=str), False),
        (int, exp.AnyType(equals=str, map_before=lambda x: str), True),
        # test optional
        (None, exp.AnyType(), False),
        (None, exp.AnyType(optional=True), True),
        # test vars
        (ABC, exp.AnyType(vars={"a": 1}), False),
        (ABC, exp.AnyType(vars=exp.Dict(superset_of={"a": 1})), True),
        # test predicate
        (int, exp.AnyType(satisfies=lambda x: x == str), False),
        (str, exp.AnyType(satisfies=lambda x: x == str), True),
        # test type
        (Collection, exp.AnyType(subclass_of=list), False),
        (list, exp.AnyType(subclass_of=Collection), True),
        (list, exp.AnyType(subclass_of=list), True),
        (list, exp.AnyType(superclass_of=Collection), False),
        (Collection, exp.AnyType(superclass_of=list), True),
        (list, exp.AnyType(superclass_of=list), True),
    ],
)
def test_any_type(value, expect, result):
    assert (value == expect) == result

from collections import Collection

import pytest

import expyct as exp


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
        # test predicate
        (1, exp.Any(pred=lambda x: x % 2 == 0), False),
        (2, exp.Any(pred=lambda x: x % 2 == 0), True),
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
        # test predicate
        (1, exp.AnyValue(pred=lambda x: x % 2 == 0), False),
        (2, exp.AnyValue(pred=lambda x: x % 2 == 0), True),
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
        # test predicate
        (int, exp.AnyType(pred=lambda x: x == str), False),
        (str, exp.AnyType(pred=lambda x: x == str), True),
        # test type
        (list, exp.AnyType(subclass_of=Collection), True),
        (list, exp.AnyType(superclass_of=Collection), False),
        (Collection, exp.AnyType(subclass_of=list), False),
        (Collection, exp.AnyType(superclass_of=list), True),
        (list, exp.AnyType(superclass_of=list), True),
        (list, exp.AnyType(subclass_of=list), True),
    ],
)
def test_any_type(value, expect, result):
    assert (value == expect) == result

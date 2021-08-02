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
        (1, exp.AnyClass(), False),
        ("abc", exp.AnyClass(), False),
        ([], exp.AnyClass(), False),
        (int, exp.AnyClass(), True),
        (lambda x: x + 1, exp.AnyClass(), False),
        # test map before and equals
        (int, exp.AnyClass(equals=str), False),
        (int, exp.AnyClass(equals=str, map_before=lambda x: str), True),
        # test predicate
        (int, exp.AnyClass(pred=lambda x: x == str), False),
        (str, exp.AnyClass(pred=lambda x: x == str), True),
    ],
)
def test_any_type(value, expect, result):
    assert (value == expect) == result

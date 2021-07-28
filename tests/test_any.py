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
    ]
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
    ]
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
    ]
)
def test_any_type(value, expect, result):
    assert (value == expect) == result

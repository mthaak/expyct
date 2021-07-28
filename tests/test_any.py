import pytest

import expyct as exp


@pytest.mark.parametrize(
    ["value", "expect", "should_match"],
    [
        # test type
        (1, exp.Any(), True),
        ("abc", exp.Any(), True),
        ([], exp.Any(), True),
        (int, exp.Any(), True),
        (lambda x: x + 1, exp.Any(), True),
    ]
)
def test_any(value, expect, should_match):
    assert (value == expect) == should_match


@pytest.mark.parametrize(
    ["value", "expect", "should_match"],
    [
        # test type
        (1, exp.AnyValue(), True),
        ("abc", exp.AnyValue(), True),
        ([], exp.AnyValue(), True),
        (int, exp.AnyValue(), False),
        (lambda x: x + 1, exp.AnyValue(), False),
    ]
)
def test_any_value(value, expect, should_match):
    assert (value == expect) == should_match


@pytest.mark.parametrize(
    ["value", "expect", "should_match"],
    [
        # test type
        (1, exp.AnyType(), False),
        ("abc", exp.AnyType(), False),
        ([], exp.AnyType(), False),
        (int, exp.AnyType(), True),
        (lambda x: x + 1, exp.AnyType(), False),
    ]
)
def test_any_type(value, expect, should_match):
    assert (value == expect) == should_match

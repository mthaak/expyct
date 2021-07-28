import pytest

import expyct as exp


@pytest.mark.parametrize(
    ["value", "expect", "should_match"],
    [
        (1, exp.OneOf([1]), True),
        (1, exp.OneOf([2]), False),
        (1, exp.OneOf([]), False),
        (1, exp.OneOf([1, 2, 3]), True),
        (2, exp.OneOf([1, 2, 3]), True),
        (2, exp.OneOf({1, 2, 3}), True),
        (4, exp.OneOf({1, 2, 3}), False),
        ("c", exp.OneOf("abc"), True),
        ("d", exp.OneOf("abc"), False),
    ]
)
def test_one_of(value, expect, should_match):
    assert (value == expect) == should_match

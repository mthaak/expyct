import pytest

import expyct as exp


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        (1, exp.OneOf([]), False),
        (1, exp.OneOf([2]), False),
        (1, exp.OneOf([1]), True),
        (4, exp.OneOf({1, 2, 3}), False),
        (1, exp.OneOf([1, 2, 3]), True),
        (2, exp.OneOf([1, 2, 3]), True),
        (2, exp.OneOf({1, 2, 3}), True),
        ("d", exp.OneOf("abc"), False),
        ("c", exp.OneOf("abc"), True),
    ],
)
def test_one_of(value, expect, result):
    assert (value == expect) == result

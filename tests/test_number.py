import pytest as pytest

import expyct as exp


@pytest.mark.parametrize(
    ["value", "expect", "should_match"],
    [
        # test type
        (1, exp.Number(), True),
        (1.2, exp.Number(), True),
        ("abc", exp.Number(), False),
        # test map before
        ("1", exp.Number(map_before=int), True),
        ("abc", exp.Number(map_before=int), False),
        ("abc", exp.Number(map_before=str), False),
        # test pred
        (1, exp.Number(pred=lambda x: x % 2 == 1), True),
        (1, exp.Number(pred=lambda x: x % 2 == 0), False),
        # test min
        (2, exp.Number(min=1), True),
        (2, exp.Number(min=2), True),
        (2, exp.Number(min=3), False),
        # test max
        (2, exp.Number(max=3), True),
        (2, exp.Number(max=2), True),
        (2, exp.Number(max=1), False),
        # test min strict
        (2, exp.Number(min_strict=1), True),
        (2, exp.Number(min_strict=2), False),
        (2, exp.Number(min_strict=3), False),
        # test max strict
        (2, exp.Number(max_strict=3), True),
        (2, exp.Number(max_strict=2), False),
        (2, exp.Number(max_strict=1), False),
    ]
)
def test_number(value, expect, should_match):
    assert (value == expect) == should_match


@pytest.mark.parametrize(
    ["value", "expect", "should_match"],
    [
        # test type
        (1, exp.Int(), True),
        (1.2, exp.Int(), False),
        ("abc", exp.Int(), False),

    ]
)
def test_int(value, expect, should_match):
    assert (value == expect) == should_match


@pytest.mark.parametrize(
    ["value", "expect", "should_match"],
    [
        # test type
        (1, exp.Float(), False),
        (1.2, exp.Float(), True),
        ("abc", exp.Float(), False),

    ]
)
def test_float(value, expect, should_match):
    assert (value == expect) == should_match

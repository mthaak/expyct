from numbers import Number as ParentNumber

import pytest as pytest

import expyct as exp


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        ("abc", exp.Number(), False),
        (1, exp.Number(), True),
        (1.2, exp.Number(), True),
        # test map before
        ("abc", exp.Number(map_before=int), False),
        ("abc", exp.Number(map_before=str), False),
        ("1", exp.Number(map_before=int), True),
        # test optional
        (None, exp.Number(), False),
        (None, exp.Number(optional=True), True),
        # test instance
        (1, exp.Number(type=int), True),
        (1, exp.Number(type=float), False),
        (1, exp.Number(instance_of=int), True),
        (1, exp.Number(instance_of=float), False),
        # test equals
        (1, exp.Number(equals=2), False),
        (1, exp.Number(equals=1), True),
        # test satisfies
        (1, exp.Number(satisfies=lambda x: x % 2 == 0), False),
        (1, exp.Number(satisfies=lambda x: x % 2 == 1), True),
        # test min
        (2, exp.Number(min=3), False),
        (2, exp.Number(min=2), True),
        (2, exp.Number(min=1), True),
        # test max
        (2, exp.Number(max=1), False),
        (2, exp.Number(max=2), True),
        (2, exp.Number(max=3), True),
        # test min strict
        (2, exp.Number(min_strict=3), False),
        (2, exp.Number(min_strict=2), False),
        (2, exp.Number(min_strict=1), True),
        # test max strict
        (2, exp.Number(max_strict=1), False),
        (2, exp.Number(max_strict=2), False),
        (2, exp.Number(max_strict=3), True),
        # test close to
        (2, exp.Number(close_to=1.5), False),
        (0.8, exp.Number(close_to=1), False),
        (1.2, exp.Number(close_to=1), False),
        (1, exp.Number(close_to=1), True),
        (0.8, exp.Number(close_to=1, error=0.1), False),
        (1.2, exp.Number(close_to=1, error=0.1), False),
        (0.8, exp.Number(close_to=1, error=0.3), True),
        (1.2, exp.Number(close_to=1, error=0.3), True),
    ],
)
def test_number_eq(value, expect, result):
    assert (value == expect) == result


@pytest.mark.xfail  # TODO not yet implemented
def test_number_instance():
    obj: ParentNumber = exp.Number()
    assert isinstance(obj, ParentNumber)


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        ("abc", exp.Int(), False),
        (1, exp.Int(), True),
        (1.2, exp.Int(), False),
    ],
)
def test_int_eq(value, expect, result):
    assert (value == expect) == result


def test_int_instance():
    obj: int = exp.Int()
    assert isinstance(obj, int)


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        ("abc", exp.Float(), False),
        (1, exp.Float(), False),
        (1.2, exp.Float(), True),
    ],
)
def test_float_eq(value, expect, result):
    assert (value == expect) == result


def test_float_instance():
    obj: float = exp.Float()
    assert isinstance(obj, float)

from collections.abc import Collection

import pytest
from dataclasses import dataclass

import expyct as exp


@dataclass(init=True)
class ABC:
    a: int = 1
    b: int = 2
    c: int = 3

    def __eq__(self, other):
        if not isinstance(other, ABC):
            return False
        return vars(self) == vars(other)


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test no args
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
        (ABC(1, 2, 3), exp.Any(vars={"x": 4}), False),
        (ABC(1, 2, 3), exp.Any(vars=exp.Dict(length=3)), True),
        # test satisfies
        (1, exp.Any(satisfies=lambda x: x % 2 == 0), False),
        (2, exp.Any(satisfies=lambda x: x % 2 == 0), True),
        # test type
        (1, exp.Any(type=float), False),
        (2, exp.Any(type=int), True),
        # test instance_of
        (ABC(), exp.Any(instance_of=dict), False),
        (ABC(), exp.Any(instance_of=object), True),
    ],
)
def test_any(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test no args
        (1, exp.AnyValue(), True),
        ("abc", exp.AnyValue(), True),
        ([], exp.AnyValue(), True),
        (int, exp.AnyValue(), False),
        (lambda x: x + 1, exp.AnyValue(), False),
        # test type
        ("abc", exp.AnyValue(type=int), False),
        (4, exp.AnyValue(type=int), True),
        (ABC(1, 2, 3), exp.AnyValue(type=ABC), True),
        # test map before and equals
        (1, exp.AnyValue(equals=2), False),
        (1, exp.AnyValue(equals=2, map_before=lambda x: x + 1), True),
        # test optional
        (None, exp.AnyValue(), False),
        (None, exp.AnyValue(optional=True), True),
        # test equals
        (1, exp.AnyValue(equals=2), False),
        (2, exp.AnyValue(equals=2), True),
        (ABC(1, 2, 3), exp.AnyValue(equals=ABC(4, 5, 6)), False),
        (ABC(4, 5, 6), exp.AnyValue(equals=ABC(4, 5, 6)), True),
        # test vars
        (ABC(1, 2, 3), exp.AnyValue(vars={"x": 4}), False),
        (ABC(1, 2, 3), exp.AnyValue(vars=exp.Dict(length=3)), True),
        # test satisfies
        (1, exp.AnyValue(satisfies=lambda x: x % 2 == 0), False),
        (2, exp.AnyValue(satisfies=lambda x: x % 2 == 0), True),
        # test type
        (1, exp.AnyValue(type=float), False),
        (2, exp.AnyValue(type=int), True),
        # test instance_of
        (ABC(), exp.AnyValue(instance_of=dict), False),
        (ABC(), exp.AnyValue(instance_of=object), True),
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
        # test satisfies
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

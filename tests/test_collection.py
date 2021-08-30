from collections import defaultdict

import pytest

import expyct as exp


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (list(), exp.Collection(), True),
        (tuple(), exp.Collection(), True),
        (set(), exp.Collection(), True),
        (dict(), exp.Collection(), True),
        ("abc", exp.Collection(), True),
        (1, exp.Collection(), False),
        # test instance
        (list(), exp.Collection(type=list), True),
        (tuple(), exp.Collection(type=list), False),
        (defaultdict(int), exp.Collection(instance_of=dict), True),
        (defaultdict(int), exp.Collection(type=dict), False),
        (list, exp.Collection(instance_of=dict), False),
        (tuple(), exp.Collection(type=list), False),
        # test map before
        (1, exp.Collection(map_before=lambda x: [x]), True),
        # test optional
        (None, exp.Collection(), False),
        (None, exp.Collection(optional=True), True),
        # test equals
        ([1, 2, 3], exp.Collection(equals=[1, 2, 3]), True),
        ([1, 2, 3], exp.Collection(equals=[1, 2]), False),
        # test length
        ([1, 2, 3], exp.Collection(length=3), True),
        ([1, 2, 3], exp.Collection(length=2), False),
        # test min length
        ([1, 2], exp.Collection(min_length=3), False),
        ([1, 2, 3], exp.Collection(min_length=3), True),
        ([1, 2, 3, 4], exp.Collection(min_length=3), True),
        # test max length
        ([1, 2], exp.Collection(max_length=3), True),
        ([1, 2, 3], exp.Collection(max_length=3), True),
        ([1, 2, 3, 4], exp.Collection(max_length=3), False),
        # test non empty
        ([1, 2], exp.Collection(non_empty=True), True),
        ([], exp.Collection(non_empty=True), False),
        # test subset of
        ([1, 2], exp.Collection(subset_of=[1, 2, 3]), True),
        ([1, 2, 4], exp.Collection(subset_of=[1, 2, 3]), False),
        # test superset of
        ([1, 2, 3], exp.Collection(superset_of=[1, 2]), True),
        ([1, 3], exp.Collection(superset_of=[1, 2]), False),
        # test predicate
        ([1, 2, 3, 4], exp.Collection(satisfies=lambda x: sum(x) == 10), True),
        ([1, 2, 3, 4], exp.Collection(satisfies=lambda x: len(x) == 10), False),
        # test all
        ([1, 2, 3, 4], exp.Collection(all=2), False),
        ([2, 2, 2], exp.Collection(all=2), True),
        # test any
        ([1, 2, 3, 4], exp.Collection(any=5), False),
        ([2, 5, 2], exp.Collection(any=5), True),
    ],
)
def test_collection(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (list(), exp.List(), True),
        (tuple(), exp.List(), False),
        (set(), exp.List(), False),
        (dict(), exp.List(), False),
        ("abc", exp.List(), False),
        (1, exp.List(), False),
        # test map before
        (1, exp.List(map_before=lambda x: [x]), True),
        # test optional
        (None, exp.List(), False),
        (None, exp.List(optional=True), True),
        # test equals
        ([1, 2, 3], exp.List(equals=[1, 2, 3]), True),
        ([1, 2, 3], exp.List(equals=[1, 2]), False),
        # test equals with ignore order
        ([1, 2, 3], exp.List(equals=[3, 2, 1], ignore_order=False), False),
        ([1, 2, 3], exp.List(equals=[3, 2, 1], ignore_order=True), True),
        # test length
        ([1, 2, 3], exp.List(length=3), True),
        ([1, 2, 3], exp.List(length=2), False),
        # test min length
        ([1, 2], exp.List(min_length=3), False),
        ([1, 2, 3], exp.List(min_length=3), True),
        ([1, 2, 3, 4], exp.List(min_length=3), True),
        # test max length
        ([1, 2], exp.List(max_length=3), True),
        ([1, 2, 3], exp.List(max_length=3), True),
        ([1, 2, 3, 4], exp.List(max_length=3), False),
        # test non empty
        ([1, 2], exp.List(non_empty=True), True),
        ([], exp.List(non_empty=True), False),
        # test subset of
        ([1, 2], exp.List(subset_of=[1, 2, 3]), True),
        ([1, 2, 4], exp.List(subset_of=[1, 2, 3]), False),
        # test superset of
        ([1, 2, 3], exp.List(superset_of=[1, 2]), True),
        ([1, 3], exp.List(superset_of=[1, 2]), False),
        # test predicate
        ([1, 2, 3, 4], exp.List(satisfies=lambda x: sum(x) == 10), True),
        ([1, 2, 3, 4], exp.List(satisfies=lambda x: len(x) == 10), False),
        # test all
        ([1, 2, 3, 4], exp.List(all=2), False),
        ([2, 2, 2], exp.List(all=2), True),
        # test any
        ([1, 2, 3, 4], exp.List(any=5), False),
        ([2, 5, 2], exp.List(any=5), True),
    ],
)
def test_list(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (list(), exp.Tuple(), False),
        (tuple(), exp.Tuple(), True),
        (set(), exp.Tuple(), False),
        (dict(), exp.Tuple(), False),
        ("abc", exp.Tuple(), False),
        (1, exp.Tuple(), False),
        # test map before
        (1, exp.Tuple(map_before=lambda x: (x,)), True),
        # test optional
        (None, exp.Tuple(), False),
        (None, exp.Tuple(optional=True), True),
        # test equals
        ((1, 2, 3), exp.Tuple(equals=(1, 2, 3)), True),
        ((1, 2, 3), exp.Tuple(equals=(1, 2)), False),
        # test length
        ((1, 2, 3), exp.Tuple(length=3), True),
        ((1, 2, 3), exp.Tuple(length=2), False),
        # test min length
        ((1, 2), exp.Tuple(min_length=3), False),
        ((1, 2, 3), exp.Tuple(min_length=3), True),
        ((1, 2, 3, 4), exp.Tuple(min_length=3), True),
        # test max length
        ((1, 2), exp.Tuple(max_length=3), True),
        ((1, 2, 3), exp.Tuple(max_length=3), True),
        ((1, 2, 3, 4), exp.Tuple(max_length=3), False),
        # test non empty
        ((1, 2), exp.Tuple(non_empty=True), True),
        ((), exp.Tuple(non_empty=True), False),
        # test subset of
        ((1, 2), exp.Tuple(subset_of=(1, 2, 3)), True),
        ((1, 2, 4), exp.Tuple(subset_of=(1, 2, 3)), False),
        # test superset of
        ((1, 2, 3), exp.Tuple(superset_of=(1, 2)), True),
        ((1, 3), exp.Tuple(superset_of=(1, 2)), False),
        # test predicate
        ((1, 2, 3, 4), exp.Tuple(satisfies=lambda x: sum(x) == 10), True),
        ((1, 2, 3, 4), exp.Tuple(satisfies=lambda x: len(x) == 10), False),
        # test all
        ((1, 2, 3, 4), exp.Tuple(all=2), False),
        ((2, 2, 2), exp.Tuple(all=2), True),
        # test any
        ((1, 2, 3, 4), exp.Tuple(any=5), False),
        ((2, 5, 2), exp.Tuple(any=5), True),
    ],
)
def test_tuple(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (list(), exp.Set(), False),
        (tuple(), exp.Set(), False),
        (set(), exp.Set(), True),
        (dict(), exp.Set(), False),
        ("abc", exp.Set(), False),
        (1, exp.Set(), False),
        # test map before
        (1, exp.Set(map_before=lambda x: {x}), True),
        # test optional
        (None, exp.Set(), False),
        (None, exp.Set(optional=True), True),
        # test equals
        ({1, 2, 3}, exp.Set(equals={1, 2, 3}), True),
        ({1, 2, 3}, exp.Set(equals={1, 2}), False),
        # test length
        ({1, 2, 3}, exp.Set(length=3), True),
        ({1, 2, 3}, exp.Set(length=2), False),
        # test min length
        ({1, 2}, exp.Set(min_length=3), False),
        ({1, 2, 3}, exp.Set(min_length=3), True),
        ({1, 2, 3, 4}, exp.Set(min_length=3), True),
        # test max length
        ({1, 2}, exp.Set(max_length=3), True),
        ({1, 2, 3}, exp.Set(max_length=3), True),
        ({1, 2, 3, 4}, exp.Set(max_length=3), False),
        # test non empty
        ({1, 2}, exp.Set(non_empty=True), True),
        ({}, exp.Set(non_empty=True), False),
        # test subset of
        ({1, 2}, exp.Set(subset_of={1, 2, 3}), True),
        ({1, 2, 4}, exp.Set(subset_of={1, 2, 3}), False),
        # test superset of
        ({1, 2, 3}, exp.Set(superset_of={1, 2}), True),
        ({1, 3}, exp.Set(superset_of={1, 2}), False),
        # test predicate
        ({1, 2, 3, 4}, exp.Set(satisfies=lambda x: sum(x) == 10), True),
        ({1, 2, 3, 4}, exp.Set(satisfies=lambda x: len(x) == 10), False),
        # test all
        ({1, 2, 3, 4}, exp.Set(all=2), False),
        ({2, 2, 2}, exp.Set(all=2), True),
        # test any
        ({1, 2, 3, 4}, exp.Set(any=5), False),
        ({2, 5, 2}, exp.Set(any=5), True),
    ],
)
def test_set(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (list(), exp.Dict(), False),
        (tuple(), exp.Dict(), False),
        (set(), exp.Dict(), False),
        (dict(), exp.Dict(), True),
        ("abc", exp.Dict(), False),
        (1, exp.Dict(), False),
        # test map before
        (1, exp.Dict(map_before=lambda x: {x: "a"}), True),
        # test optional
        (None, exp.Dict(), False),
        (None, exp.Dict(optional=True), True),
        # test equals
        ({1: "a", 2: "b", 3: "c"}, exp.Dict(equals={1: "a", 2: "b", 3: "c"}), True),
        ({1: "a", 2: "b", 3: "c"}, exp.Dict(equals={1: "a", 2: "b"}), False),
        # test length
        ({1: "a", 2: "b", 3: "c"}, exp.Dict(length=3), True),
        ({1: "a", 2: "b", 3: "c"}, exp.Dict(length=2), False),
        # test min length
        ({1: "a", 2: "b"}, exp.Dict(min_length=3), False),
        ({1: "a", 2: "b", 3: "c"}, exp.Dict(min_length=3), True),
        ({1: "a", 2: "b", 3: "c", 4: "d"}, exp.Dict(min_length=3), True),
        # test max length
        ({1: "a", 2: "b"}, exp.Dict(max_length=3), True),
        ({1: "a", 2: "b", 3: "c"}, exp.Dict(max_length=3), True),
        ({1: "a", 2: "b", 3: "c", 4: "d"}, exp.Dict(max_length=3), False),
        # test non empty
        ({1: "a", 2: "b"}, exp.Dict(non_empty=True), True),
        ({}, exp.Dict(non_empty=True), False),
        # test subset of
        ({1: "a", 2: "b"}, exp.Dict(subset_of={1: "a", 2: "b", 3: "c"}), True),
        ({1: "a", 2: "b", 4: "d"}, exp.Dict(subset_of={1: "a", 2: "b", 3: "c"}), False),
        # test superset of
        ({1: "a", 2: "b", 3: "c"}, exp.Dict(superset_of={1: "a", 2: "b"}), True),
        ({1: "a", 3: "c"}, exp.Dict(superset_of={1: "a", 2: "b"}), False),
        # test predicate
        ({1: "a", 2: "b", 3: "c", 4: "d"}, exp.Dict(satisfies=lambda x: sum(x) == 10), True),
        ({1: "a", 2: "b", 3: "c", 4: "d"}, exp.Dict(satisfies=lambda x: len(x) == 10), False),
        # test keys all
        ({1: "a", 2: "b", 3: "c", "4": "d"}, exp.Dict(keys_all=exp.ANY_INT), False),
        ({1: "a", 2: "b", 3: "c", 4: "d"}, exp.Dict(keys_all=exp.ANY_INT), True),
        # test keys any
        ({1: "a", 2: "b", 3: "c", 4: "d"}, exp.Dict(keys_any=5), False),
        ({1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}, exp.Dict(keys_any=5), True),
        # test values all
        ({1: "a", 2: "b", 3: "c", 4: "d"}, exp.Dict(values_all="a"), False),
        ({1: "a", 2: "a", 3: "a", 4: "a"}, exp.Dict(values_all="a"), True),
        # test values any
        ({1: "a", 2: "b", 3: "c", 4: "d"}, exp.Dict(values_any="e"), False),
        ({1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}, exp.Dict(values_any="e"), True),
    ],
)
def test_dict(value, expect, result):
    assert (value == expect) == result

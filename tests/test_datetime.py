from datetime import datetime, date, time, timedelta, timezone

import pytest

import expyct as exp
from expyct import parse_isoformat


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (datetime(2020, 1, 1), exp.DateTime(), True),
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTime(), True),
        (date(2020, 1, 1), exp.DateTime(), False),
        (time(3, 2, 1), exp.DateTime(), False),
        ("abc", exp.DateTime(), False),
        # test equals
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTime(equals=datetime(2020, 1, 1, 3, 2, 1)), True),
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTime(equals=datetime(2020, 1, 1, 3, 2, 2)), False),
        # test before and after
        (datetime(2020, 3, 3), exp.DateTime(after=datetime(2020, 1, 1)), True),
        (datetime(2020, 3, 3), exp.DateTime(after=datetime(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.DateTime(after=datetime(2020, 3, 4)), False),
        (datetime(2020, 3, 3), exp.DateTime(before=datetime(2020, 1, 1)), False),
        (datetime(2020, 3, 3), exp.DateTime(before=datetime(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.DateTime(before=datetime(2020, 3, 4)), True),
        # test predicate
        (datetime(2020, 3, 3), exp.DateTime(pred=lambda x: x.year == 2020), True),
        (datetime(2020, 3, 3), exp.DateTime(pred=lambda x: x.year == 2021), False),
    ],
)
def test_datetime(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (datetime(2020, 1, 1), exp.Date(), False),
        (datetime(2020, 1, 1, 3, 2, 1), exp.Date(), False),
        (date(2020, 1, 1), exp.Date(), True),
        (time(3, 2, 1), exp.Date(), False),
        ("abc", exp.Date(), False),
        # test equals
        (date(2020, 1, 1), exp.Date(equals=date(2020, 1, 1)), True),
        (date(2020, 1, 1), exp.Date(equals=date(2020, 1, 2)), False),
        # test before and after
        (date(2020, 3, 3), exp.Date(after=date(2020, 1, 1)), True),
        (date(2020, 3, 3), exp.Date(after=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.Date(after=date(2020, 3, 4)), False),
        (date(2020, 3, 3), exp.Date(before=date(2020, 1, 1)), False),
        (date(2020, 3, 3), exp.Date(before=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.Date(before=date(2020, 3, 4)), True),
        # test predicate
        (date(2020, 3, 3), exp.Date(pred=lambda x: x.year == 2020), True),
        (date(2020, 3, 3), exp.Date(pred=lambda x: x.year == 2021), False),
    ],
)
def test_date(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (datetime(2020, 1, 1), exp.Time(), False),
        (datetime(2020, 1, 1, 3, 2, 1), exp.Time(), False),
        (date(2020, 1, 1), exp.Time(), False),
        (time(3, 2, 1), exp.Time(), True),
        ("abc", exp.Time(), False),
        # test equals
        (time(3, 2, 1), exp.Time(equals=time(3, 2, 1)), True),
        (time(3, 2, 1), exp.Time(equals=time(3, 2, 2)), False),
        # test before and after
        (time(3, 3), exp.Time(after=time(1, 1)), True),
        (time(3, 3), exp.Time(after=time(3, 3)), False),
        (time(3, 3), exp.Time(after=time(3, 4)), False),
        (time(3, 3), exp.Time(before=time(1, 1)), False),
        (time(3, 3), exp.Time(before=time(3, 3)), False),
        (time(3, 3), exp.Time(before=time(3, 4)), True),
        # test predicate
        (time(3, 3), exp.Time(pred=lambda x: x.hour == 3), True),
        (time(3, 3), exp.Time(pred=lambda x: x.hour == 2), False),
    ],
)
def test_time(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (datetime(2020, 1, 1), exp.AnyDateTime(), True),
        (datetime(2020, 1, 1, 3, 2, 1), exp.AnyDateTime(), True),
        (date(2020, 1, 1), exp.AnyDateTime(), True),
        (time(3, 2, 1), exp.AnyDateTime(), True),
        ("abc", exp.AnyDateTime(), False),
        # test map before
        ("2020-01-01", exp.AnyDateTime(equals=date(2020, 1, 1), map_before=parse_isoformat), True),
        ("01:01:03", exp.AnyDateTime(equals=time(1, 1, 3), map_before=parse_isoformat), True),
        (
            "2020-01-01T01:01:03",
            exp.AnyDateTime(
                equals=datetime(2020, 1, 1, 1, 1, 3, tzinfo=timezone.utc),
                map_before=parse_isoformat,
            ),
            True,
        ),
        (
            "2020-01-01T01:01:03+00:00",
            exp.AnyDateTime(
                equals=datetime(2020, 1, 1, 1, 1, 3, tzinfo=timezone.utc),
                map_before=parse_isoformat,
            ),
            True,
        ),
        (
            date(2020, 1, 1),
            exp.AnyDateTime(equals=date(2020, 1, 1), map_before=parse_isoformat),
            False,
        ),
        # test equals
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTime(equals=datetime(2020, 1, 1, 3, 2, 1)), True),
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTime(equals=datetime(2020, 1, 1, 3, 2, 2)), False),
        (date(2020, 1, 1), exp.AnyDateTime(equals=date(2020, 1, 1)), True),
        (date(2020, 1, 1), exp.AnyDateTime(equals=date(2020, 1, 2)), False),
        (time(3, 2, 1), exp.AnyDateTime(equals=time(3, 2, 1)), True),
        (time(3, 2, 1), exp.AnyDateTime(equals=time(3, 2, 2)), False),
        # test instance
        (datetime(2020, 1, 1), exp.AnyDateTime(type=datetime), True),
        (datetime(2020, 1, 1), exp.AnyDateTime(type=date), False),
        (datetime(2020, 1, 1), exp.AnyDateTime(instance_of=datetime), True),
        (datetime(2020, 1, 1), exp.AnyDateTime(instance_of=date), True),
        ("abc", exp.AnyDateTime(instance_of=datetime), False),
        # test before and after
        # both given and bound is datetime
        (datetime(2020, 3, 3), exp.AnyDateTime(after=datetime(2020, 1, 1)), True),
        (datetime(2020, 3, 3), exp.AnyDateTime(after=datetime(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.AnyDateTime(after=datetime(2020, 3, 4)), False),
        (datetime(2020, 3, 3), exp.AnyDateTime(before=datetime(2020, 1, 1)), False),
        (datetime(2020, 3, 3), exp.AnyDateTime(before=datetime(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.AnyDateTime(before=datetime(2020, 3, 4)), True),
        # datetime is given but bound is date
        (datetime(2020, 3, 3), exp.AnyDateTime(after=date(2020, 1, 1)), True),
        (datetime(2020, 3, 3), exp.AnyDateTime(after=date(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.AnyDateTime(after=date(2020, 3, 4)), False),
        (datetime(2020, 3, 3), exp.AnyDateTime(before=date(2020, 1, 1)), False),
        (datetime(2020, 3, 3), exp.AnyDateTime(before=date(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.AnyDateTime(before=date(2020, 3, 4)), True),
        # datetime is given but bound is time
        (datetime(2020, 3, 3), exp.AnyDateTime(after=time(1, 1)), False),
        # date is given but bound is datetime
        (date(2020, 3, 3), exp.AnyDateTime(after=datetime(2020, 1, 1)), False),
        # both given and bound is date
        (date(2020, 3, 3), exp.AnyDateTime(after=date(2020, 1, 1)), True),
        (date(2020, 3, 3), exp.AnyDateTime(after=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.AnyDateTime(after=date(2020, 3, 4)), False),
        (date(2020, 3, 3), exp.AnyDateTime(before=date(2020, 1, 1)), False),
        (date(2020, 3, 3), exp.AnyDateTime(before=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.AnyDateTime(before=date(2020, 3, 4)), True),
        # date is given but bound is time
        (date(2020, 3, 3), exp.AnyDateTime(after=time(1, 1)), False),
        # time is given but bound is datetime`
        (time(3, 3), exp.AnyDateTime(after=datetime(2020, 1, 1)), False),
        # time is given but bound is date
        (time(3, 3), exp.AnyDateTime(after=date(2020, 1, 1)), False),
        # both given and bound is time
        (time(3, 3), exp.AnyDateTime(after=time(1, 1)), True),
        (time(3, 3), exp.AnyDateTime(after=time(3, 3)), False),
        (time(3, 3), exp.AnyDateTime(after=time(3, 4)), False),
        (time(3, 3), exp.AnyDateTime(before=time(1, 1)), False),
        (time(3, 3), exp.AnyDateTime(before=time(3, 3)), False),
        (time(3, 3), exp.AnyDateTime(before=time(3, 4)), True),
        # timedelta
        (
            datetime.now().astimezone(timezone.utc) + timedelta(seconds=-3),
            exp.AnyDateTime(after=timedelta(seconds=-2)),
            False,
        ),
        (
            datetime.now().astimezone(timezone.utc) + timedelta(seconds=-1),
            exp.AnyDateTime(after=timedelta(seconds=-2)),
            True,
        ),
        (
            datetime.now().astimezone(timezone.utc) + timedelta(seconds=3),
            exp.AnyDateTime(before=timedelta(seconds=2)),
            False,
        ),
        (
            datetime.now().astimezone(timezone.utc) + timedelta(seconds=1),
            exp.AnyDateTime(before=timedelta(seconds=2)),
            True,
        ),
        # test predicate
        (datetime(2020, 3, 3), exp.DateTime(pred=lambda x: x.year == 2020), True),
        (datetime(2020, 3, 3), exp.DateTime(pred=lambda x: x.year == 2021), False),
    ],
)
def test_any_datetime(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["dt", "expect"],
    [
        ("2020-01-01", date(2020, 1, 1)),
        ("01:01:03", time(1, 1, 3)),
        ("2020-01-01T01:01:03", datetime(2020, 1, 1, 1, 1, 3, tzinfo=timezone.utc)),
        ("2020-01-01T01:01:03+00:00", datetime(2020, 1, 1, 1, 1, 3, tzinfo=timezone.utc)),
    ],
)
def test_parse_isoformat(dt, expect):
    assert parse_isoformat(dt) == expect

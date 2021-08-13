from datetime import datetime, date, time, timedelta, timezone

import pytest

import expyct as exp
from expyct import parse_isoformat

UTC = timezone.utc


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (datetime(2020, 1, 1), exp.DateTime(), True),
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTime(), True),
        (datetime(2020, 1, 1, 3, 2, 1, tzinfo=UTC), exp.DateTime(), True),
        (date(2020, 1, 1), exp.DateTime(), False),
        (time(3, 2, 1), exp.DateTime(), False),
        ("abc", exp.DateTime(), False),
        # test map_before
        (
            "2020-01-01T01:01:03",
            exp.DateTime(
                equals=datetime(2020, 1, 1, 1, 1, 3, tzinfo=UTC),
                map_before=parse_isoformat,
            ),
            True,
        ),
        # test equals
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTime(equals=datetime(2020, 1, 1, 3, 2, 1)), True),
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTime(equals=datetime(2020, 1, 1, 3, 2, 2)), False),
        # test before and after
        (datetime(2020, 3, 3), exp.DateTime(after_strict=datetime(2020, 1, 1)), True),
        (datetime(2020, 3, 3), exp.DateTime(after_strict=datetime(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.DateTime(after_strict=datetime(2020, 3, 4)), False),
        (datetime(2020, 3, 3), exp.DateTime(before_strict=datetime(2020, 1, 1)), False),
        (datetime(2020, 3, 3), exp.DateTime(before_strict=datetime(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.DateTime(before_strict=datetime(2020, 3, 4)), True),
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
        (datetime(2020, 1, 1), exp.DateTimeTz(), False),
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTimeTz(), False),
        (datetime(2020, 1, 1, 3, 2, 1, tzinfo=UTC), exp.DateTimeTz(), True),
        (date(2020, 1, 1), exp.DateTimeTz(), False),
        (time(3, 2, 1), exp.DateTimeTz(), False),
        ("abc", exp.DateTimeTz(), False),
        # test map_before
        (
            "2020-01-01T01:01:03+00:00",
            exp.DateTimeTz(
                equals=datetime(2020, 1, 1, 1, 1, 3, tzinfo=UTC),
                map_before=parse_isoformat,
            ),
            True,
        ),
        # test equals
        (
            datetime(2020, 1, 1, 3, 2, 1, tzinfo=UTC),
            exp.DateTimeTz(equals=datetime(2020, 1, 1, 3, 2, 1, tzinfo=UTC)),
            True,
        ),
        (
            datetime(2020, 1, 1, 3, 2, 1, tzinfo=UTC),
            exp.DateTimeTz(equals=datetime(2020, 1, 1, 3, 2, 2, tzinfo=UTC)),
            False,
        ),
        # test before and after
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(after=datetime(2020, 1, 1, tzinfo=UTC)),
            True,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(after=datetime(2020, 3, 3, tzinfo=UTC)),
            True,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(after=datetime(2020, 3, 4, tzinfo=UTC)),
            False,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(before=datetime(2020, 1, 1, tzinfo=UTC)),
            False,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(before=datetime(2020, 3, 3, tzinfo=UTC)),
            True,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(before=datetime(2020, 3, 4, tzinfo=UTC)),
            True,
        ),
        # timedelta
        (
            datetime.now().astimezone(UTC) + timedelta(seconds=-3),
            exp.DateTimeTz(after=timedelta(seconds=-2)),
            False,
        ),
        (
            datetime.now().astimezone(UTC) + timedelta(seconds=-1),
            exp.DateTimeTz(after=timedelta(seconds=-2)),
            True,
        ),
        (
            datetime.now().astimezone(UTC) + timedelta(seconds=3),
            exp.DateTimeTz(before=timedelta(seconds=2)),
            False,
        ),
        (
            datetime.now().astimezone(UTC) + timedelta(seconds=1),
            exp.DateTimeTz(before=timedelta(seconds=2)),
            True,
        ),
        # test before and after strict
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(after_strict=datetime(2020, 1, 1, tzinfo=UTC)),
            True,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(after_strict=datetime(2020, 3, 3, tzinfo=UTC)),
            False,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(after_strict=datetime(2020, 3, 4, tzinfo=UTC)),
            False,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(before_strict=datetime(2020, 1, 1, tzinfo=UTC)),
            False,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(before_strict=datetime(2020, 3, 3, tzinfo=UTC)),
            False,
        ),
        (
            datetime(2020, 3, 3, tzinfo=UTC),
            exp.DateTimeTz(before_strict=datetime(2020, 3, 4, tzinfo=UTC)),
            True,
        ),
        # timedelta
        (
            datetime.now().astimezone(UTC) + timedelta(seconds=-3),
            exp.DateTimeTz(after_strict=timedelta(seconds=-2)),
            False,
        ),
        (
            datetime.now().astimezone(UTC) + timedelta(seconds=-1),
            exp.DateTimeTz(after_strict=timedelta(seconds=-2)),
            True,
        ),
        (
            datetime.now().astimezone(UTC) + timedelta(seconds=3),
            exp.DateTimeTz(before_strict=timedelta(seconds=2)),
            False,
        ),
        (
            datetime.now().astimezone(UTC) + timedelta(seconds=1),
            exp.DateTimeTz(before_strict=timedelta(seconds=2)),
            True,
        ),
        # test predicate
        (datetime(2020, 3, 3, tzinfo=UTC), exp.DateTimeTz(pred=lambda x: x.year == 2020), True),
        (datetime(2020, 3, 3, tzinfo=UTC), exp.DateTimeTz(pred=lambda x: x.year == 2021), False),
    ],
)
def test_datetime_tz(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (datetime(2020, 1, 1), exp.Date(), False),
        (datetime(2020, 1, 1, 3, 2, 1), exp.Date(), False),
        (datetime(2020, 1, 1, 3, 2, 1, tzinfo=UTC), exp.Date(), False),
        (date(2020, 1, 1), exp.Date(), True),
        (time(3, 2, 1), exp.Date(), False),
        ("abc", exp.Date(), False),
        # test map before
        ("2020-01-01", exp.Date(equals=date(2020, 1, 1), map_before=parse_isoformat), True),
        # test equals
        (date(2020, 1, 1), exp.Date(equals=date(2020, 1, 1)), True),
        (date(2020, 1, 1), exp.Date(equals=date(2020, 1, 2)), False),
        # test before and after
        (date(2020, 3, 3), exp.Date(after=date(2020, 1, 1)), True),
        (date(2020, 3, 3), exp.Date(after=date(2020, 3, 3)), True),
        (date(2020, 3, 3), exp.Date(after=date(2020, 3, 4)), False),
        (date(2020, 3, 3), exp.Date(before=date(2020, 1, 1)), False),
        (date(2020, 3, 3), exp.Date(before=date(2020, 3, 3)), True),
        (date(2020, 3, 3), exp.Date(before=date(2020, 3, 4)), True),
        # test before and after strict
        (date(2020, 3, 3), exp.Date(after_strict=date(2020, 1, 1)), True),
        (date(2020, 3, 3), exp.Date(after_strict=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.Date(after_strict=date(2020, 3, 4)), False),
        (date(2020, 3, 3), exp.Date(before_strict=date(2020, 1, 1)), False),
        (date(2020, 3, 3), exp.Date(before_strict=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.Date(before_strict=date(2020, 3, 4)), True),
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
        (datetime(2020, 1, 1, 3, 2, 1, tzinfo=UTC), exp.Date(), False),
        (date(2020, 1, 1), exp.Time(), False),
        (time(3, 2, 1), exp.Time(), True),
        ("abc", exp.Time(), False),
        # test map before
        ("01:01:03", exp.Time(equals=time(1, 1, 3), map_before=parse_isoformat), True),
        # test equals
        (time(3, 2, 1), exp.Time(equals=time(3, 2, 1)), True),
        (time(3, 2, 1), exp.Time(equals=time(3, 2, 2)), False),
        # test before and after
        (time(3, 3), exp.Time(after=time(1, 1)), True),
        (time(3, 3), exp.Time(after=time(3, 3)), True),
        (time(3, 3), exp.Time(after=time(3, 4)), False),
        (time(3, 3), exp.Time(before=time(1, 1)), False),
        (time(3, 3), exp.Time(before=time(3, 3)), True),
        (time(3, 3), exp.Time(before=time(3, 4)), True),
        # test before and after strict
        (time(3, 3), exp.Time(after_strict=time(1, 1)), True),
        (time(3, 3), exp.Time(after_strict=time(3, 3)), False),
        (time(3, 3), exp.Time(after_strict=time(3, 4)), False),
        (time(3, 3), exp.Time(before_strict=time(1, 1)), False),
        (time(3, 3), exp.Time(before_strict=time(3, 3)), False),
        (time(3, 3), exp.Time(before_strict=time(3, 4)), True),
        # test predicate
        (time(3, 3), exp.Time(pred=lambda x: x.hour == 3), True),
        (time(3, 3), exp.Time(pred=lambda x: x.hour == 2), False),
    ],
)
def test_time(value, expect, result):
    assert (value == expect) == result


@pytest.mark.parametrize(
    ["dt", "expect"],
    [
        ("2020-01-01", date(2020, 1, 1)),
        ("01:01:03", time(1, 1, 3)),
        ("2020-01-01T01:01:03", datetime(2020, 1, 1, 1, 1, 3, tzinfo=UTC)),
        ("2020-01-01T01:01:03+00:00", datetime(2020, 1, 1, 1, 1, 3, tzinfo=UTC)),
        ("2020-01-01T01:01:03Z", datetime(2020, 1, 1, 1, 1, 3, tzinfo=UTC)),
    ],
)
def test_parse_isoformat(dt, expect):
    assert parse_isoformat(dt) == expect

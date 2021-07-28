from datetime import datetime, date, time, timedelta

import pytest

import expyct as exp


@pytest.mark.parametrize(
    ["value", "expect", "result"],
    [
        # test type
        (datetime(2020, 1, 1), exp.DateTime(), True),
        (datetime(2020, 1, 1, 3, 2, 1), exp.DateTime(), True),
        (date(2020, 1, 1), exp.DateTime(), False),
        (time(3, 2, 1), exp.DateTime(), False),
        ("abc", exp.DateTime(), False),
        # test before and after
        (datetime(2020, 3, 3), exp.DateTime(after=datetime(2020, 1, 1)), True),
        (datetime(2020, 3, 3), exp.DateTime(after=datetime(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.DateTime(after=datetime(2020, 3, 4)), False),
        (datetime(2020, 3, 3), exp.DateTime(before=datetime(2020, 1, 1)), False),
        (datetime(2020, 3, 3), exp.DateTime(before=datetime(2020, 3, 3)), False),
        (datetime(2020, 3, 3), exp.DateTime(before=datetime(2020, 3, 4)), True),
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
        # test before and after
        (date(2020, 3, 3), exp.Date(after=date(2020, 1, 1)), True),
        (date(2020, 3, 3), exp.Date(after=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.Date(after=date(2020, 3, 4)), False),
        (date(2020, 3, 3), exp.Date(before=date(2020, 1, 1)), False),
        (date(2020, 3, 3), exp.Date(before=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.Date(before=date(2020, 3, 4)), True),
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
        # test before and after
        (time(3, 3), exp.Time(after=time(1, 1)), True),
        (time(3, 3), exp.Time(after=time(3, 3)), False),
        (time(3, 3), exp.Time(after=time(3, 4)), False),
        (time(3, 3), exp.Time(before=time(1, 1)), False),
        (time(3, 3), exp.Time(before=time(3, 3)), False),
        (time(3, 3), exp.Time(before=time(3, 4)), True),
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
        (datetime(2020, 3, 3), exp.AnyDateTime(after=time(1, 1)), ValueError),
        # date is given but bound is datetime
        (date(2020, 3, 3), exp.AnyDateTime(after=datetime(2020, 1, 1)), ValueError),
        # both given and bound is date
        (date(2020, 3, 3), exp.AnyDateTime(after=date(2020, 1, 1)), True),
        (date(2020, 3, 3), exp.AnyDateTime(after=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.AnyDateTime(after=date(2020, 3, 4)), False),
        (date(2020, 3, 3), exp.AnyDateTime(before=date(2020, 1, 1)), False),
        (date(2020, 3, 3), exp.AnyDateTime(before=date(2020, 3, 3)), False),
        (date(2020, 3, 3), exp.AnyDateTime(before=date(2020, 3, 4)), True),
        # date is given but bound is time
        (date(2020, 3, 3), exp.AnyDateTime(after=time(1, 1)), ValueError),
        # time is given but bound is datetime
        (time(3, 3), exp.AnyDateTime(after=datetime(2020, 1, 1)), ValueError),
        # time is given but bound is date
        (time(3, 3), exp.AnyDateTime(after=date(2020, 1, 1)), ValueError),
        # both given and bound is time
        (time(3, 3), exp.AnyDateTime(after=time(1, 1)), True),
        (time(3, 3), exp.AnyDateTime(after=time(3, 3)), False),
        (time(3, 3), exp.AnyDateTime(after=time(3, 4)), False),
        (time(3, 3), exp.AnyDateTime(before=time(1, 1)), False),
        (time(3, 3), exp.AnyDateTime(before=time(3, 3)), False),
        (time(3, 3), exp.AnyDateTime(before=time(3, 4)), True),
        # timedelta
        (
                datetime.now() + timedelta(seconds=-3),
                exp.AnyDateTime(after=timedelta(seconds=-2)),
                False,
        ),
        (
                datetime.now() + timedelta(seconds=-1),
                exp.AnyDateTime(after=timedelta(seconds=-2)),
                True,
        ),
        (
                datetime.now() + timedelta(seconds=3),
                exp.AnyDateTime(before=timedelta(seconds=2)),
                False,
        ),
        (datetime.now() + timedelta(seconds=1), exp.AnyDateTime(before=timedelta(seconds=2)), True),
    ],
)
def test_any_datetime(value, expect, result):
    if type(result) == type and issubclass(result, Exception):
        with pytest.raises(result):
            value == expect
    else:
        assert (value == expect) == result

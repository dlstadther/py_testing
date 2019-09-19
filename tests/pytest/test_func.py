"""
Module docstring goes here
"""
import datetime

import pytest

from py_testing.func import bom, eom


@pytest.mark.parametrize("in_date, expected_date", [
    pytest.param(datetime.date(2019, 10, 15), datetime.date(2019, 10, 1), id='2019-10'),
    pytest.param(datetime.date(2019, 2, 15), datetime.date(2019, 2, 1), id='2019-02'),
])
def test_bom(in_date, expected_date):
    """
    Test BOM func
    :param in_date: input to func
    :param expected_date: expected output to func
    """
    assert bom(in_date) == expected_date


@pytest.mark.parametrize("in_date, expected_date", [
    pytest.param(datetime.date(2019, 10, 15), datetime.date(2019, 10, 31), id='2019-10'),
    pytest.param(datetime.date(2019, 2, 15), datetime.date(2019, 2, 28), id='2019-02'),
    pytest.param(datetime.date(2020, 2, 15), datetime.date(2020, 2, 29), id='2020-02'),
])
def test_eom(in_date, expected_date):
    """
    Test EOM func
    :param in_date: input to func
    :param expected_date: expected output to func
    """
    assert eom(in_date) == expected_date

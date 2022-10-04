"""
this docstring line just needs to exceed 120 characters so to fail the pep8 verification to ensure it is working correctly
"""
import calendar
import datetime

CONST_UPPER = "CONSTANT"
const_lower = "constant"
constCamel = "constAnt"
ConstPascal = "ConstAnt"


def bom(the_date: datetime.date) -> datetime.date:
    """
    Return the first day of the month for a provided date
    :param the_date: datetime.date
    :return: first day of month for `the_date`
    """
    return the_date.replace(day=1)


def eom(the_date: datetime.date) -> datetime.date:
    """
    Return last day of month, given input date
    :param the_date: datetime.date
    :return: last day of month for `the_date`
    """
    the_year = the_date.year
    the_month = the_date.month
    the_day = calendar.monthrange(the_year, the_month)[1]
    return datetime.date(the_year, the_month, the_day)


def failure() -> None:
    """
    Do nothing
    :return: an object of datatype other than expected mypy type
    """
    return 1


def invalidFunctionName():
    # pylint: disable=C0111
    return


class ValidClassName:
    """Non-empty class docstring"""
    X = 'mystring'

    def test_1(self):
        """
        Test 1
        :return: class attribute `X`
        """
        return self.X

    def test_2(self):
        """
        Test 2
        :return: string which includes the result of `test_1()`
        """
        return f"{self.test_1()} again"


# TODO: verify in linting results
class inValidClassName(ValidClassName):
    """"""
    pass

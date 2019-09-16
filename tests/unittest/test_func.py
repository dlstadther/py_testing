import datetime
import unittest

from py_testing.func import bom, eom


class TestFunc(unittest.TestCase):

    def test_bom(self):
        in_dates = (
            (datetime.date(2019, 2, 15), datetime.date(2019, 2, 1)),
            (datetime.date(2019, 10, 15), datetime.date(2019, 10, 1)),
        )

        for in_d, expected_d in in_dates:
            with self.subTest():
                self.assertEquals(bom(in_d), expected_d)

    def test_eom(self):
        in_dates = (
            (datetime.date(2019, 2, 15), datetime.date(2019, 2, 28)),
            (datetime.date(2019, 10, 15), datetime.date(2019, 10, 31)),
            (datetime.date(2020, 2, 15), datetime.date(2020, 2, 29)),
        )

        for in_d, expected_d in in_dates:
            with self.subTest():
                self.assertEquals(eom(in_d), expected_d)

    def test_fail(self):
        self.assertEquals(0, 1)


if __name__ == '__main__':
    unittest.main()

import pytz
from datetime import datetime
from time import sleep

import pendulum

from .. import AbstractTestCase


class ComparisonTest(AbstractTestCase):

    def test_equal_to_true(self):
        d1 = pendulum.create(2000, 1, 1, 1, 2, 3)
        d2 = pendulum.create(2000, 1, 1, 1, 2, 3)
        d3 = datetime(2000, 1, 1, 1, 2, 3, tzinfo= pendulum.UTC)

        self.assertEqual(d1, d2)
        self.assertEqual(d1, d3)

    def test_equal_to_false(self):
        d1 = pendulum.create(2000, 1, 1, 1, 2, 3)
        d2 = pendulum.create(2000, 1, 2, 1, 2, 3)
        d3 = datetime(2000, 1, 2, 1, 2, 3, tzinfo= pendulum.UTC)

        self.assertNotEqual(d1, d2)
        self.assertNotEqual(d1, d3)

    def test_equal_with_timezone_true(self):
        d1 = pendulum.create(2000, 1, 1, 12, 0, 0, tz='America/Toronto')
        d2 = pendulum.create(2000, 1, 1, 9, 0, 0, tz='America/Vancouver')
        d3 = datetime(2000, 1, 1, 12, 0, 0,
                      tzinfo= pendulum.timezone('America/Toronto'))

        self.assertEqual(d1, d2)
        self.assertEqual(d1, d3)

    def test_equal_with_timezone_false(self):
        d1 = pendulum.create(2000, 1, 1, tz='America/Toronto')
        d2 = pendulum.create(2000, 1, 1, tz='America/Vancouver')
        d3 = datetime(2000, 1, 1, tzinfo= pendulum.timezone('America/Toronto'))

        self.assertNotEqual(d1, d2)
        self.assertEqual(d1, d3)

    def test_not_equal_to_true(self):
        d1 = pendulum.create(2000, 1, 1, 1, 2, 3)
        d2 = pendulum.create(2000, 1, 2, 1, 2, 3)
        d3 = datetime(2000, 1, 2, 1, 2, 3, tzinfo= pendulum.UTC)

        self.assertNotEqual(d1, d2)
        self.assertNotEqual(d1, d3)

    def test_not_equal_to_false(self):
        d1 = pendulum.create(2000, 1, 1, 1, 2, 3)
        d2 = pendulum.create(2000, 1, 1, 1, 2, 3)
        d3 = datetime(2000, 1, 1, 1, 2, 3, tzinfo= pendulum.UTC)

        self.assertEqual(d1, d2)
        self.assertEqual(d1, d3)

    def test_not_equal_with_timezone_true(self):
        d1 = pendulum.create(2000, 1, 1, tz='America/Toronto')
        d2 = pendulum.create(2000, 1, 1, tz='America/Vancouver')
        d3 = datetime(2000, 1, 1, tzinfo= pendulum.timezone('America/Toronto'))

        self.assertNotEqual(d1, d2)
        self.assertEqual(d1, d3)

    def test_not_equal_to_none(self):
        d1 = pendulum.create(2000, 1, 1, 1, 2, 3)

        self.assertNotEqual(d1, None)

    def test_greater_than_true(self):
        d1 = pendulum.create(2000, 1, 1)
        d2 = pendulum.create(1999, 12, 31)
        d3 = datetime(1999, 12, 31, tzinfo= pendulum.UTC)

        self.assertTrue(d1 > d2)
        self.assertTrue(d1 > d3)

    def test_greater_than_false(self):
        d1 = pendulum.create(2000, 1, 1)
        d2 = pendulum.create(2000, 1, 2)
        d3 = datetime(2000, 1, 2, tzinfo= pendulum.UTC)

        self.assertFalse(d1 > d2)
        self.assertFalse(d1 > d3)

    def test_greater_than_with_timezone_true(self):
        d1 = pendulum.create(2000, 1, 1, 12, 0, 0, tz='America/Toronto')
        d2 = pendulum.create(2000, 1, 1, 8, 59, 59, tz='America/Vancouver')
        d3 = pytz.timezone('America/Vancouver').localize(datetime(2000, 1, 1, 8, 59, 59))

        self.assertTrue(d1 > d2)
        self.assertTrue(d1 > d3)

    def test_greater_than_with_timezone_false(self):
        d1 = pendulum.create(2000, 1, 1, 12, 0, 0, tz='America/Toronto')
        d2 = pendulum.create(2000, 1, 1, 9, 0, 1, tz='America/Vancouver')
        d3 = pytz.timezone('America/Vancouver').localize(datetime(2000, 1, 1, 9, 0, 1))

        self.assertFalse(d1 > d2)
        self.assertFalse(d1 > d3)

    def test_greater_than_or_equal_true(self):
        d1 = pendulum.create(2000, 1, 1)
        d2 = pendulum.create(1999, 12, 31)
        d3 = datetime(1999, 12, 31, tzinfo= pendulum.UTC)

        self.assertTrue(d1 >= d2)
        self.assertTrue(d1 >= d3)

    def test_greater_than_or_equal_true_equal(self):
        d1 = pendulum.create(2000, 1, 1)
        d2 = pendulum.create(2000, 1, 1)
        d3 = datetime(2000, 1, 1, tzinfo= pendulum.UTC)

        self.assertTrue(d1 >= d2)
        self.assertTrue(d1 >= d3)

    def test_greater_than_or_equal_false(self):
        d1 = pendulum.create(2000, 1, 1)
        d2 = pendulum.create(2000, 1, 2)
        d3 = datetime(2000, 1, 2, tzinfo= pendulum.UTC)

        self.assertFalse(d1 >= d2)
        self.assertFalse(d1 >= d3)

    def test_greater_than_or_equal_with_timezone_true(self):
        d1 = pendulum.create(2000, 1, 1, 12, 0, 0, tz='America/Toronto')
        d2 = pendulum.create(2000, 1, 1, 8, 59, 59, tz='America/Vancouver')
        d3 = pytz.timezone('America/Vancouver').localize(datetime(2000, 1, 1, 8, 59, 59))

        self.assertTrue(d1 >= d2)
        self.assertTrue(d1 >= d3)

    def test_greater_than_or_equal_with_timezone_false(self):
        d1 = pendulum.create(2000, 1, 1, 12, 0, 0, tz='America/Toronto')
        d2 = pendulum.create(2000, 1, 1, 9, 0, 1, tz='America/Vancouver')
        d3 = pytz.timezone('America/Vancouver').localize(datetime(2000, 1, 1, 9, 0, 1))

        self.assertFalse(d1 >= d2)
        self.assertFalse(d1 >= d3)

    def test_less_than_true(self):
        d1 = pendulum.create(2000, 1, 1)
        d2 = pendulum.create(2000, 1, 2)
        d3 = datetime(2000, 1, 2, tzinfo= pendulum.UTC)

        self.assertTrue(d1 < d2)
        self.assertTrue(d1 < d3)

    def test_less_than_false(self):
        d1 = pendulum.create(2000, 1, 2)
        d2 = pendulum.create(2000, 1, 1)
        d3 = datetime(2000, 1, 1, tzinfo= pendulum.UTC)

        self.assertFalse(d1 < d2)
        self.assertFalse(d1 < d3)

    def test_less_than_with_timezone_true(self):
        d1 = pendulum.create(2000, 1, 1, 8, 59, 59, tz='America/Vancouver')
        d2 = pendulum.create(2000, 1, 1, 12, 0, 0, tz='America/Toronto')
        d3 = pytz.timezone('America/Toronto').localize(datetime(2000, 1, 1, 12, 0, 0))

        self.assertTrue(d1 < d2)
        self.assertTrue(d1 < d3)

    def test_less_than_with_timezone_false(self):
        d1 = pendulum.create(2000, 1, 1, 9, 0, 1, tz='America/Vancouver')
        d2 = pendulum.create(2000, 1, 1, 12, 0, 0, tz='America/Toronto')
        d3 = pytz.timezone('America/Toronto').localize(datetime(2000, 1, 1, 12, 0, 0))

        self.assertFalse(d1 < d2)
        self.assertFalse(d1 < d3)

    def test_less_than_or_equal_true(self):
        d1 = pendulum.create(2000, 1, 1)
        d2 = pendulum.create(2000, 1, 2)
        d3 = datetime(2000, 1, 2, tzinfo= pendulum.UTC)

        self.assertTrue(d1 <= d2)
        self.assertTrue(d1 <= d3)

    def test_less_than_or_equal_true_equal(self):
        d1 = pendulum.create(2000, 1, 1)
        d2 = pendulum.create(2000, 1, 1)
        d3 = datetime(2000, 1, 1, tzinfo= pendulum.UTC)

        self.assertTrue(d1 <= d2)
        self.assertTrue(d1 <= d3)

    def test_less_than_or_equal_false(self):
        d1 = pendulum.create(2000, 1, 2)
        d2 = pendulum.create(2000, 1, 1)
        d3 = datetime(2000, 1, 1, tzinfo= pendulum.UTC)

        self.assertFalse(d1 <= d2)
        self.assertFalse(d1 <= d3)

    def test_less_than_or_equal_with_timezone_true(self):
        d1 = pendulum.create(2000, 1, 1, 8, 59, 59, tz='America/Vancouver')
        d2 = pendulum.create(2000, 1, 1, 12, 0, 0, tz='America/Toronto')
        d3 = pytz.timezone('America/Toronto').localize(datetime(2000, 1, 1, 12, 0, 0))

        self.assertTrue(d1 <= d2)
        self.assertTrue(d1 <= d3)

    def test_less_than_or_equal_with_timezone_false(self):
        d1 = pendulum.create(2000, 1, 1, 9, 0, 1, tz='America/Vancouver')
        d2 = pendulum.create(2000, 1, 1, 12, 0, 0, tz='America/Toronto')
        d3 = pytz.timezone('America/Toronto').localize(datetime(2000, 1, 1, 12, 0, 0))

        self.assertFalse(d1 <= d2)
        self.assertFalse(d1 <= d3)

    def test_is_birthday(self):
        with self.wrap_with_test_now():
            d = pendulum.now()
            a_birthday = d.subtract(years=1)
            self.assertTrue(a_birthday.is_birthday())
            not_a_birthday = d.subtract(days=1)
            self.assertFalse(not_a_birthday.is_birthday())
            also_not_a_birthday = d.add(days=2)
            self.assertFalse(also_not_a_birthday.is_birthday())

        d1 = pendulum.create(1987, 4, 23)
        d2 = pendulum.create(2014, 9, 26)
        d3 = pendulum.create(2014, 4, 23)
        self.assertFalse(d2.is_birthday(d1))
        self.assertTrue(d3.is_birthday(d1))

    def test_closest(self):
        instance = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt1 = pendulum.create(2015, 5, 28, 11, 0, 0)
        dt2 = pendulum.create(2015, 5, 28, 14, 0, 0)
        closest = instance.closest(dt1, dt2)
        self.assertEqual(dt1, closest)

        closest = instance.closest(dt2, dt1)
        self.assertEqual(dt1, closest)

    def test_closest_with_datetime(self):
        instance = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt1 = datetime(2015, 5, 28, 11, 0, 0)
        dt2 = datetime(2015, 5, 28, 14, 0, 0)
        closest = instance.closest(dt1, dt2)
        self.assertIsInstanceOfDateTime(closest)
        self.assertDateTime(closest, 2015, 5, 28, 11, 0, 0)

    def test_closest_with_equals(self):
        instance = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt1 = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt2 = pendulum.create(2015, 5, 28, 14, 0, 0)
        closest = instance.closest(dt1, dt2)
        self.assertEqual(dt1, closest)

    def test_farthest(self):
        instance = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt1 = pendulum.create(2015, 5, 28, 11, 0, 0)
        dt2 = pendulum.create(2015, 5, 28, 14, 0, 0)
        closest = instance.farthest(dt1, dt2)
        self.assertEqual(dt2, closest)

        closest = instance.farthest(dt2, dt1)
        self.assertEqual(dt2, closest)

    def test_farthest_with_datetime(self):
        instance = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt1 = datetime(2015, 5, 28, 11, 0, 0, tzinfo= pendulum.UTC)
        dt2 = datetime(2015, 5, 28, 14, 0, 0, tzinfo= pendulum.UTC)
        closest = instance.farthest(dt1, dt2)
        self.assertIsInstanceOfDateTime(closest)
        self.assertDateTime(closest, 2015, 5, 28, 14, 0, 0)

    def test_farthest_with_equals(self):
        instance = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt1 = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt2 = pendulum.create(2015, 5, 28, 14, 0, 0)
        closest = instance.farthest(dt1, dt2)
        self.assertEqual(dt2, closest)

    def test_is_same_day(self):
        dt1 = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt2 = pendulum.create(2015, 5, 29, 12, 0, 0)
        dt3 = pendulum.create(2015, 5, 28, 12, 0, 0)
        dt4 = datetime(2015, 5, 28, 12, 0, 0, tzinfo= pendulum.UTC)
        dt5 = datetime(2015, 5, 29, 12, 0, 0, tzinfo= pendulum.UTC)

        self.assertFalse(dt1.is_same_day(dt2))
        self.assertTrue(dt1.is_same_day(dt3))
        self.assertTrue(dt1.is_same_day(dt4))
        self.assertFalse(dt1.is_same_day(dt5))

    def test_comparison_to_unsupported(self):
        dt1 = pendulum.now()

        self.assertFalse(dt1 == 'test')
        self.assertFalse(dt1 in ['test'])

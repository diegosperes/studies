from unittest import TestCase
from google.sum_numbers.solution import sum_numbers


class SumNumbers(TestCase):

    def test_sum_numbers(self):
        self.assertEqual(123, sum_numbers('abc123xyz'))
        self.assertEqual(44, sum_numbers('aa11b33'))
        self.assertEqual(18, sum_numbers('7 11'))

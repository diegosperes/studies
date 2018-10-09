from unittest import TestCase
from google.max_span.solution import max_span


class MaxSpan(TestCase):

    def test_max_span_with_4(self):
        self.assertEqual(4, max_span([1, 2, 1, 1, 3]))

    def test_max_span_with_6(self):
        self.assertEqual(6, max_span([1, 4, 2, 1, 4, 1, 4]))
        self.assertEqual(6, max_span([1, 4, 2, 1, 4, 4, 4]))

from unittest import TestCase
from google.without_string.solution import without_string


class WithoutString(TestCase):

    def setUp(self):
        self.base = 'Hello there'

    def test_do_not_change_string_when_does_not_has_remove_character(self):
        self.assertEqual(without_string(self.base, 'x'), 'Hello there')

    def test_remove_one_character(self):
        self.assertEqual(without_string(self.base, 'e'), 'Hllo thr')

    def test_remove_more_than_one_character(self):
        self.assertEqual(without_string(self.base, 'llo'), 'He there')

    def test_remove_only_string(self):
        self.assertEqual(without_string(self.base, 'lo'), 'Hel there')

    def test_remove_multiple_strings(self):
        self.assertEqual(without_string('hellolo there', 'lo'), 'hel there')
        self.assertEqual(without_string('lolololololololololololo', 'lo'), '')

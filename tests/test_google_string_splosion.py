from unittest import TestCase
from google.string_splosion.solution import string_splosion


class StringSplosion(TestCase):

    def test_string_splosion_with_word_code(self):
        self.assertEqual('CCoCodCode', string_splosion('Code'))

    def test_string_splosion_with_word_abc(self):
        self.assertEqual('aababc', string_splosion('abc'))

    def test_string_splosion_with_word_ab(self):
        self.assertEqual('aab', string_splosion('ab'))

import time
from unittest import TestCase
from google.decompress_string.solution import decompress


class DecompressString(TestCase):

    def setUp(self):
        self.maxDiff = None

    def test_decompresss_expression_with_one_element(self):
        self.assertEqual('aaaaaaaaaa', decompress('10[a]'))

    def test_decompresss_expression_with_two_elements(self):
        self.assertEqual('ababababab', decompress('5[ab]'))

    def test_decompresss_expression_without_number(self):
        self.assertEqual('ab', decompress('[ab]'))

    def test_decompresss_sibling_expression(self):
        self.assertEqual('abcabcabcababababc', decompress('3[abc]4[ab]c'))

    def test_decompresss_expression_inside_another(self):
        self.assertEqual('ababc' * 3, decompress('3[2[ab]c]'))
        self.assertEqual('ababcababcababcd' * 4, decompress('4[3[2[ab]c]d]'))

    def test_decompresss_expression_inside_another_with_siblings(self):
        self.assertEqual('ababcababcababcddddd', decompress('3[2[ab]c]5[d]'))

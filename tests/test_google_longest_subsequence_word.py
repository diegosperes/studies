from unittest import TestCase
from google.longest_subsequence_word.solution import solution, Sequence


class TrieTree:
    def values(self):
        return ['able', 'ale', 'apple', 'bale', 'kangaroo']


class StringSequenceModel(TestCase):

    def test_is_subsequence(self):
        string = Sequence('fadjuitcegnso')
        self.assertTrue(string.is_subsequence('juice'))

    def test_is_not_subsequence(self):
        string = Sequence('fadjuitcegnso')
        self.assertFalse(string.is_subsequence('tango'))

    def test_is_valid(self):
        word = Sequence('car')
        [word.increment() for index in range(3)]
        self.assertTrue(word.is_valid())

    def test_is_not_valid(self):
        word = Sequence('car')
        self.assertFalse(word.is_valid())
        [word.increment() for index in range(4)]
        self.assertFalse(word.is_valid())

    def test_check_if_sequence_over(self):
        word = Sequence('car')
        self.assertTrue(word.was_not_ended())
        [word.increment() for index in range(3)]
        self.assertFalse(word.was_not_ended())


class LongestSubsequenceWord(TestCase):

    def test_solution_with_set(self):
        string = 'abppplee'
        words = {'able', 'ale', 'apple', 'bale', 'kangaroo'}
        self.assertEqual('apple', solution(string, words))

    def test_solution_with_hash_table(self):
        string = 'abppplee'
        words = {1 : 'able', 2 : 'ale', 3 : 'apple', 4 : 'bale', 5 : 'kangaroo'}
        self.assertEqual('apple', solution(string, words))

    def test_solution_with_list(self):
        string = 'abppplee'
        words = ['able', 'ale', 'apple', 'bale', 'kangaroo']
        self.assertEqual('apple', solution(string, words))

    def test_solution_with_trie_tree(self):
        string = 'abppplee'
        words = TrieTree()
        self.assertEqual('apple', solution(string, words))

    def test_raise_exception_when_words_type_is_not_valid(self):
        self.assertRaises(TypeError, solution, 'abppplee', '')
        self.assertRaises(TypeError, solution, 'abppplee', iter([]))

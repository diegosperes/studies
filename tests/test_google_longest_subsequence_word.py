from unittest import TestCase
from google.longest_subsequence_word.solution import solution


class TrieTree:
    def values(self):
        return ['able', 'ale', 'apple', 'bale', 'kangaroo']


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

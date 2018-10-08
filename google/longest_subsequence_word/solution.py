

class Sequence:
    def __init__(self, pattern):
        self._optimize = {}
        for index, char in enumerate(pattern):
            self._optimize.setdefault(char, [])
            self._optimize[char].append(index)

    def is_subsequence(self, word):
        self._index = -1
        for char in word:
            if not self._has(char):
                return False
        return True

    def _has(self, char):
        indices = [index for index in self._optimize.get(char, []) if index > self._index]
        if not indices:
            return False
        self._index = indices[0]
        return True


def find_longest_subsequence(string, words):
    if type(words) not in [list, set, dict] and not hasattr(words, 'values'):
        raise TypeError()
    elif type(words) not in [list, set]:
        words = words.values()

    result = None
    pattern = Sequence(string)
    for word in words:
        is_bigger = not result or len(word) > len(result)
        if is_bigger and pattern.is_subsequence(word):
            result = word
    return result

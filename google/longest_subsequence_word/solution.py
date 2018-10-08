

class Sequence:
    @property
    def value(self):
        return self._value[self._index]

    def __init__(self, value):
        self.length = len(value)
        self._value = value
        self._index = 0

    def was_not_ended(self):
        return self.length > self._index

    def increment(self):
        self._index += 1

    def is_valid(self):
        return self.length == self._index

    def is_subsequence(self, word):
        self._reset()
        word = Sequence(word)
        while self.length > word.length and word.was_not_ended() and self.was_not_ended():
            if self.value == word.value:
                word.increment()
            self.increment()

        if word.is_valid():
            return True
        return False

    def _reset(self):
        self._index = 0


def solution(string, words):
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

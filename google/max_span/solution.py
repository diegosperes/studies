import collections


def max_span(array):
    _array = collections.defaultdict(list)
    for index, value in enumerate(array):
        _array[value].append(index)
    return max([_array[value][-1] - index + 1 for index, value in enumerate(array)])

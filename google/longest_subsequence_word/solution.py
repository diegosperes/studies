

def solution(string, words):
    result =  None
    result_length = 0
    string_length = len(string)

    if type(words) not in [list, set, dict] and not hasattr(words, 'values'):
        raise TypeError()
    elif type(words) not in [list, set]:
        words = words.values()

    for word in words:
        string_index = 0
        word_index = 0
        word_length = len(word)

        while string_length > word_length and word_length > word_index and string_length > string_index:
            if string[string_index] == word[word_index]:
                word_index += 1
            string_index += 1
        if word_index == word_length and word_length > result_length:
            result = word
            result_length = word_length

    return result

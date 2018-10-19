

def _get_expression(base, begin, end):
    number = ''
    start = begin
    digit_index = begin - 1
    while digit_index >= 0 and base[digit_index].isnumeric():
        start = digit_index
        number = base[digit_index] + number
        digit_index -= 1
    number = int(number) if number else 1
    return number, base[begin + 1: end], start


def decompress(base):
    index = 0
    result = ''
    brackets = []
    for character in base:
        result += character
        if character == ']':
            number, value, begin = _get_expression(result, brackets.pop(-1), index)
            result = result[:begin] + number * value
            index = len(result)
            continue
        elif character == '[':
            brackets.append(index)
        index += 1

    return result

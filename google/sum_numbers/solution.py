

def sum_numbers(string):
    index = 0
    result = 0
    while len(string) > index:
        sub_string = ''
        for character in string[index:]:
            if not character.isnumeric():
                break
            sub_string += character
        if sub_string:
            result += int(sub_string)
        index += len(sub_string) + 1
    return result

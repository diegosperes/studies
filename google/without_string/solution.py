

def without_string(base, remove):
    index = 0
    result = ''
    while len(base) > index:
        while base[index : index + len(remove)] == remove:
            index += len(remove)
        if len(base) > index:
            result += base[index]
        index += 1
    return result

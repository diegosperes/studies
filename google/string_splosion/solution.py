

def string_splosion(string):
    return ''.join([string[:index] + char for index, char in enumerate(string)])

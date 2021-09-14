def reverse_string(word: str) -> str:
    """
    Reverse the word.

    :param word: is a string
    :return: the reverse version of word
    >>> reverse_string("jump")
    'pmuj'
    >>> reverse_string("phone")
    'enohp'
    >>> reverse_string("yummy")
    'ymmuy'
    """
    # solution 1
    result = ''
    index = len(word) - 1
    while index >= 0:
        result += word[index]
        index -= 1
    return result

    # challenge: can you think of another implementation? 

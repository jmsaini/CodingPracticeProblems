def remove_vowels(word: str) -> str:
    """
    Remove the vowels from the word and return the word after cleaning
    :param word: the word contains vowels that need to be removed
    :return: the word after removing all the vowels
    >>> remove_vowels('JASmine')
    'JSmn'
    >>> remove_vowels('HAllOWorld')
    'HllWrld'
    """
    new_word = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for char in word:
        if char not in vowels:
            new_word += char
    return new_word

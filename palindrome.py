def is_palindrome(sentence: str) -> bool:
    """
    Find whether the sentence is a palindrome. Note that this sentence
    may not be meaningful and it may have numbers and special characters
    that need to be removed before.

    Hint: the sentence is a palindrome if the letters match
    An example of palindrome:
    - mom dad mom

    :param sentence: is a string
    :return: true if the word is a palindrome or false otherwise
    >>> is_palindrome("mom dad mom")
    True
    >>> is_palindrome("@ mo?m! 000 da.%d 111 )mom ?")
    True
    >>> is_palindrome("Hallo . @ World??/ ")
    False
    """
    clean_str = ''
    for char in sentence:
        if char.lower().isalpha():
            clean_str += char

    start = 0
    end = len(clean_str) - 1
    while start < len(clean_str) and end > 0:
        if clean_str[start] != clean_str[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

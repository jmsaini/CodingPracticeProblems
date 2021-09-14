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
    # clean the sentence by removing numbers and special characters
    clean_str = ''
    for char in sentence:
        if char.lower().isalpha():
            clean_str += char
    
    # initially compare the letter at index 0 with the last letter
    start = 0
    end = len(clean_str) - 1
    while start < len(clean_str) and end > 0:
        # returns false when the letter at start and letter at end do not match
        if clean_str[start] != clean_str[end]:
            return False
        else:
            # right letter 
            start += 1
            # left letter
            end -= 1
    # returns true if line 32 has not been executed within the loop
    return True

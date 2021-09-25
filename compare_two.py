def compare_two(str1: str, str2: str) -> bool:
    """
    Compare the two strings and return true if the two strings have the same
    sequence of characters and false if the two strings are not the same

    :param str1: string 1 contains characters that need to be compared with str2
    :param str2: string 2 contains characters that need to be compared with str1
    :return: true if the two strings match and false otherwise
    >>> compare_two("I love programming!", "I love programming!")
    True
    >>> compare_two("Learning how to code", "Learning how to code...")
    False
    """
    # note the difference between = (assignment operator) and
    # == (comparison operator)
    return str1 == str2

    #  if str1 == str2:
    #      return True
    #  else:
    #      return False

    # Challenge: find a substring in two strings that match





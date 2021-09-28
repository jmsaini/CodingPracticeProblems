from typing import Dict


def find_highest(cart: Dict) -> int:
    """
    Find the highest value that occurs in the cart.

    An example of input:
    {0: 4, 1: 15, 2: 6, 3: 0, 4: 3}

    :param cart: is a dictionary where the key is a unique number given to a
    particular item and the value is the number of times it occurs in the cart
    :return: the unique number of the item that has the highest number of occurrence in the cart, 
    return the first highest occurrence whenever there is a tie 
    >>> find_highest({0: 4, 1: 0, 2: 16, 3: 10, 4: 3})
    2
    >>> find_highest({0: 4, 1: 0, 2: 9, 3: 15, 4: 15, 5: 8, 6: 17, 7: 17})
    6
    """
    lst = list(cart.values())
    maximum = max(lst)
    find_index = lst.index(maximum)
    return find_index
    
    # Challenge: Can you optimize this solution? 

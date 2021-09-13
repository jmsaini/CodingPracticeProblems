from typing import List, Union


def delete_list(lst: List[List[int]]) -> Union[List[List[int]], List]:
    """
    Delete the last list in lst.
    Precondition: the length of lst is equal to 1 or greater than 1.

    :param lst: a nested list that contains integers.
    :return: returns a nested list if length of lst is greater than 1 or
    a list if the length is equal to 1.
    >>> delete_list([[]])
    []
    >>> delete_list([[223]])
    []
    >>> delete_list([[1], [2]])
    [[1]]
    >>> delete_list([[2, 3, 4], [5, 4], [0]])
    [[2, 3, 4], [5, 4]]
    >>> delete_list([[34], [2, 4], [5], [7, 6, 4], [0, 3], [12, 6, 89]])
    [[34], [2, 4], [5], [7, 6, 4], [0, 3]]
    """
    # len finds the length of the list
    length = len(lst)

    if length == 1:
        return []
    # remember that index always start with a zero, so we must subtract one
    # or we will get an index error
    else:
        return lst[:length - 1]

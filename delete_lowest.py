from typing import List


def delete_lowest(lst: List) -> List:
    """
    Find the lowest number in the list and remove it. Return the list.
    Note if there is more than one lowest number then remove the first
    occurrence.
    :param lst: a list of integers
    :return: return the original list with the lowest number removed
    >>> delete_lowest([823, 445, 12, 5413])
    [823, 445, 5413]
    >>> delete_lowest([394, 103, 420, 90, 65, 26, 79, 135, 380, 26, 110, 62])
    [394, 103, 420, 90, 65, 79, 135, 380, 26, 110, 62]
    """
    # start with the first num in the lst
    lowest = lst[0]
    index = 0

    # start with the second index
    for i in range(1, len(lst)):
        if lst[i] < lowest:
            lowest = lst[i]
            index = i

    lst.pop(index)
    return lst

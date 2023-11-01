#!/usr/bin/python3
"""finds a peak element from unsorted list"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: List of unsorted integers.

    Returns:
    - A peak element.

    Complexity:
    - O(log(n)) in the worst case.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    # At the end of the loop, low and high will point to a peak
    return list_of_integers[low]

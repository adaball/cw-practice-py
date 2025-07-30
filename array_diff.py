"""https://www.codewars.com/kata/523f5d21c841566fde000009/train/python"""

"""
Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

Examples

If a = [1, 2] and b = [1], the result should be [2].
If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].


computing the difference between two lists
remove all occurences of elems from list a that are present in list b
order of elements in the first list (list a) should be preserved in result


assumptions:
    - a and b are always lists
    - a and b are never None
    - a and b will always be in ASC order*****


a was [1,2,2], b was [1], expected [2,2]: [2] should equal [2, 2]
"""

def array_diff(a, b):
    a_copy = a.copy()

    for i in a:
        try:
            idx = b.index(i)
            a_copy.remove(i)
        except ValueError:
            # eat error
            pass

    return a_copy

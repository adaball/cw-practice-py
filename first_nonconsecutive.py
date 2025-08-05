"""https://www.codewars.com/kata/58f8a3a27a5c28d92e000144"""

def first_non_consecutive(arr):
    i = -1
    a = arr[i]
    b = arr[i + 1]

    while i < len(arr) - 2:
        i += 1
        a = arr[i]
        b = arr[i + 1]
        diff = b - a

        if diff != 1:
            return b

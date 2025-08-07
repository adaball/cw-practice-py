"""https://www.codewars.com/kata/55983863da40caa2c900004e"""

"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

  9 ==> -1
111 ==> -1
531 ==> -1
"""
from re import split

from itertools import permutations


def swap(s, i, j, t):
    print(f"|{"-" * t}swap({s}, {i}, {j})")
    tokens = [t for t in split("", s) if t != '']
    temp = tokens[i]
    tokens[i] = tokens[j]
    tokens[j] = temp

    ret = ""
    for token in tokens:
        ret += token

    return ret


def find_permutations(n, l, r, t):
    print(f"|{"-" * t}permutations({n}, {l}, {r}, {t})")
    s = str(n)
    perms = []

    if l == r:
        print(f"|{"-" * t}perms.append({s})")
        perms.append(s)
    else:
        for i in range(l, r + 1):
            s = swap(s, l, i, t)
            perms.extend(permutations(s, l + 1, r, t + 1))
            s = swap(s, l, i, t)

    return {int(i) for i in perms}


def next_bigger(n):
    s = str(n)
    perms = {p for p in permutations(s)}
    perms_i = []
    for p in perms:
        s = ""
        for digit in p:
            s += digit
        perms_i.append(int(s))


    perms_i = {p for p in perms_i if p > n}
    lowest = -1
    for i in perms_i:
        if lowest == -1:
            lowest = i
            continue

        if abs(n - i) < abs(n - lowest):
            lowest = i

    return lowest

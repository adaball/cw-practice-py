"""https://www.codewars.com/kata/55e86e212fce2aae75000060"""

"""
Given 4 integers a, b, c, d we form the sum of the squares of a and b 
and then the sum of the squares of c and d. We multiply the two sums 
hence a number n and we try to decompose n in a sum of two squares 
e and f (e and f integers >= 0) so that n = e² + f².

(a^2 + b^2) * (c^2 + d^2) = n

decompose n in a sum of two squares e and f (e and f integers >= 0) so 
that n = e² + f².

More: e and f must result only from sums (or differences) of products 
between on the one hand (a, b) and on the other (c, d) each of a, b, c, d 
taken only once. 

For example, prod2sum(1, 2, 1, 3) should return [[1, 7], [5, 5]]) because
1==1*3-1*2
7==2*3+1*1
5==1*2+1*3
-----
test.assert_equals(prod2sum(1, 2, 1, 3), [[1, 7], [5, 5]])
test.assert_equals(prod2sum(2, 3, 4, 5), [[2, 23], [7, 22]])
test.assert_equals(prod2sum(1, 2, 2, 3), [[1, 8], [4, 7]])
test.assert_equals(prod2sum(1, 1, 3, 5), [[2, 8]])

test.assert_equals(prod2sum(1, 20, -4, -5), [[75, 104], [85, 96]])
test.assert_equals(prod2sum(-14, 12, - 10, 8), [[8, 236], [44, 232]])
"""

from itertools import permutations

def find_possible_e_and_f(a, b, c, d):
    possible_vals = set()
    for p in permutations([a, b, c, d]):
        sum_v = p[0] * p[1] + p[2] * p[3]
        dif_v = p[0] * p[1] - p[2] * p[3]

        # nb idk why it's valid to use the abs val of negative results
        #    when the instructions say e and f must be >= 0, but this
        #    passes all the tests
        possible_vals.add(abs(sum_v))
        possible_vals.add(abs(dif_v))
    return possible_vals


def remove_dupes(arr):
    uniq = set()
    for a in arr:
        uniq.add(f"{a[0]}_{a[1]}")
    ret = [s.split("_") for s in uniq]
    return [[int(r[0]), int(r[1])] for r in ret]


def find_e_and_f(n, a, b, c, d):
    answers = []
    possible_vals = find_possible_e_and_f(a, b, c, d)
    for e in possible_vals:
        for f in possible_vals:
            if e**2 + f**2 == n:
                answers.append([e, f] if e < f else [f, e])
    return remove_dupes(answers)


def sum_of_squares(i, j):
    return i**2 + j**2


def calc_n(a, b, c, d):
    return sum_of_squares(a, b) * sum_of_squares(c, d)


def prod2sum(a, b, c, d):
    n = calc_n(a, b, c, d)
    return sorted(find_e_and_f(n, a, b, c, d))

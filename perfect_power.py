"""https://www.codewars.com/kata/54d4c8b08776e4ad92000835"""

"""
Your task is to check wheter a given integer is a perfect power. 
If it is a perfect power, return a pair m and k with m^k = n as a 
proof. Otherwise return Nothing, Nil, null, NULL, None or your 
language's equivalent.

Note: For a perfect power, there might be several pairs. For example 
81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. However, the 
tests take care of this, so if a number is a perfect power, return any 
pair that proves it.


for i in range(n)
    for j in range(n)
        result = i**j

        if result > n:
            break

        if result == n:
            return (i, j)


test.assert_equals(isPP(4), [2,2], "4 = 2^2")
test.assert_equals(isPP(9), [3,2], "9 = 3^2")
test.assert_equals(isPP(5), None, "5 isn't a perfect power")

938120019968

"""


def isPP(n):
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            ans = i**j
            if ans > n:
                break
            elif ans == n:
                return [i, j]


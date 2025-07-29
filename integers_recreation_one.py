"""https://www.codewars.com/kata/55aa075506463dac6600010d"""
import math

fd_memo = dict()

def find_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors


def find_divisors_memo(n):
    if n not in fd_memo:
        fd_memo[n] = find_divisors(n)
    return fd_memo[n]


def sum_of_squares(l):
    sum = 0
    for ll in l:
        sum += ll**2
    return sum


def is_sq(i):
    return math.sqrt(i) % 1 == 0


#two elements: first the number the squared divisors of 
# which is a square and then the sum of the squared divisors.
def list_squared(m, n):
    results = []
    for i in range(m, n + 1):
        divisors = find_divisors_memo(i)
        sq_sum = sum_of_squares(divisors)
        if is_sq(sq_sum):
            results.append([i, sq_sum])
    return results

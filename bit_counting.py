"""https://www.codewars.com/kata/526571aae218b8ee490006f4"""

from re import split

def count_bits(n):
    num_of_ones = 0

    for token in split("", bin(n)):
        if token == '1':
            num_of_ones += 1

    return num_of_ones

"""https://www.codewars.com/kata/52c4dd683bfd3b434c000292"""

"""
Return values
- a 2 if the number is "interesting" (see below)
- a 1 if an interesting number occurs within the next two miles
- a 0 if the number is not interesting.

Interesting numbers are 3-or-more digit numbers that meet one or more of the following criteria:
- Any digit followed by all zeros: 100, 90000
- Every digit is the same number: 1111
- The digits are sequential, incementing†: 1234
- The digits are sequential, decrementing‡: 4321
- The digits are a palindrome: 1221 or 73837
- The digits match one of the values in the awesome_phrases array

† For incrementing sequences, 0 should come after 9, and not before 1, as in 7890.
‡ For decrementing sequences, 0 should come after 1, and not before 9, as in 3210.

Examples:
# "boring" numbers
is_interesting(3, [1337, 256])    # 0
is_interesting(3236, [1337, 256]) # 0

# progress as we near an "interesting" number
is_interesting(11207, []) # 0
is_interesting(11208, []) # 0
is_interesting(11209, []) # 1
is_interesting(11210, []) # 1
is_interesting(11211, []) # 2

# nearing a provided "awesome phrase"
is_interesting(1335, [1337, 256]) # 1
is_interesting(1336, [1337, 256]) # 1
is_interesting(1337, [1337, 256]) # 2


check current number for interesting
check if numbers within 2 increments are interesting


tests = [
    {'n': 3, 'interesting': [1337, 256], 'expected': 0},
    {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
    {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
    {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
    {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
    {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
]
"""
from re import match


def is_palindrome(number):
    num_str = str(number)

    i = 0
    j = len(num_str) - 1
    while i < j:
        if num_str[i] != num_str[j]:
            return False

        i += 1
        j -= 1

    return True


def is_sequential_dec(number):
    num_str = str(number)

    i = 0
    while i <= len(num_str) - 2:
        curr_str = num_str[i]
        next_str = num_str[i + 1]
        expected = str(int(curr_str) - 1)

        if next_str != expected:
            return False

        i += 1

    return True


def is_sequential_inc(number):
    num_str = str(number)

    def next_expected(n):
        if n == 9:
            return "0"
        else:
            return str(n + 1)

    i = 0
    while i <= len(num_str) - 2:
        curr_str = num_str[i]
        next_str = num_str[i + 1]

        expected = next_expected(int(curr_str))
        if next_str != expected:
            return False

        i += 1

    return True


def all_same_digit(number):
    num_str = str(number)
    to_match = num_str[0]

    return all([i == to_match for i in num_str])


def followed_by_two_zeros(number):
    return match(r"^\d+[0]{2,}$", str(number)) is not None


def is_awesome_phrase(number, awesome_phrases):
    return number in awesome_phrases


def _is_interesting(number, awesome_phrases):
    if number < 100:
        return False

    return any(
        [
            followed_by_two_zeros(number),
            all_same_digit(number),
            is_sequential_inc(number),
            is_sequential_dec(number),
            is_palindrome(number),
            is_awesome_phrase(number, awesome_phrases),
        ]
    )


def is_interesting(number, awesome_phrases):
    print(number, awesome_phrases)

    n = _is_interesting(number, awesome_phrases)
    n1 = _is_interesting(number + 1, awesome_phrases)
    n2 = _is_interesting(number + 2, awesome_phrases)

    if n:
        return 2
    elif n1 or n2:
        return 1

    return 0

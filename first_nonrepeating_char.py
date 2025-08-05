"""https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python"""

"""
Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the string, and occurs first in the 
string.

As an added challenge, upper- and lowercase letters are considered the same 
character, but the function should return the correct case for the initial 
letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty 
string ("");


constraints
    - upper and lowercase characters are considered equal
    - character must be returned in its original form (so 'T' -> 'T', 
        and 't' -> 't'
    - when string contains all repeating characters, return empty string

dictionary to track all the frequencies of characters
should also track the original form of the first appearance of the character
(1, "t") -> tTTTttTTT

re.split

def first_non_repeating_letter(s)
    tokens = s.split("")
    freq_dict = dict()

    i = 0
    for token in tokens:
        lower_version = token.toLower()

        if lower_version is not in freq_dict:
            freq_dict[lower_version] = {
                "first_idx": i,
                "first_version": token,
                "count": 1
            }
        else:
            freq_dict[lower_version]["count"] = freq_dict[lower_version]["count"] + 1

    non_repeaters = []
    for v in freq_dict.values():
        if v["count"] == 1:
            non_repeaters.append((v["first_idx"], v["first_version"])

    lowest = 10000
    token = None
    for nr in non_repeaters:
        if nr[0] < lowest:
            lowest = nr[0]
            token = nr[1]

    return token

"""

from re import split

def first_non_repeating_letter(s):
    tokens = [t for t in split("", s) if t != '']
    freq_dict = dict()

    i = 0
    for token in tokens:
        lower_version = token.lower()

        if lower_version not in freq_dict:
            freq_dict[lower_version] = {
                "first_idx": i,
                "first_version": token,
                "count": 1
            }
        else:
            freq_dict[lower_version]["count"] = freq_dict[lower_version]["count"] + 1
        i += 1

    non_repeaters = []
    for v in freq_dict.values():
        if v["count"] == 1:
            non_repeaters.append((v["first_idx"], v["first_version"]))

    lowest = None
    token = ''
    for nr in non_repeaters:
        if lowest is None or nr[0] < lowest:
            lowest = nr[0]
            token = nr[1]

    return token

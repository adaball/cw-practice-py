"""https://www.codewars.com/kata/517abf86da9663f1d2000003"""


"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"The_Stealth-Warrior" gets converted to "TheStealthWarrior"


constraints:
    - delimeters are dashes '-' and underscores '_'
    - convert delimeters into camel casing
    - ONLY capitalize the first word if the ORIGINAL was capitalized
    - all words following should be capitalized

problem:
    - tokenizing the string with both delimeters
    - detect first word's capitalization
"""
from re import split

def to_camel_case(text):
    tokens = split(r"[-_]", text)
    final_s = ""
    i = 0
    while i < len(tokens):
        if i == 0:
            final_s += tokens[i]
        else:
            final_s += tokens[i].capitalize()
        i += 1

    return final_s

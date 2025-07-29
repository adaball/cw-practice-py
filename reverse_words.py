"""https://www.codewars.com/kata/5259b20d6021e9e14c0010d4"""

"""
Complete the function that accepts a string parameter, and 
reverses each word in the string. All spaces in the string 
should be retained.
"""
def reverse_word(s):
    rev_str = ""
    s_len = len(s)
    i = s_len - 1

    while i >= 0:
        rev_str += s[i]
        i -= 1

    return rev_str

def reverse_words(s):
    rev_words = []

    final_s = ""
    curr_word = ""
    for token in s:
        if token == " ":
            final_s += reverse_word(curr_word)
            final_s += token

            curr_word = ""
            continue

        curr_word += token

    final_s += reverse_word(curr_word)

    return final_s

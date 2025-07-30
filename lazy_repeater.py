"""https://www.codewars.com/kata/51fc3beb41ecc97ee20000c3"""


"""
The makeLooper() function (or make_looper in your language) takes a string 
(of non-zero length) as an argument. It returns a function. The function 
it returns will return successive characters of the string on successive 
invocations. It will start back at the beginning of the string once it 
reaches the end.

For example:

abc = make_looper('abc')
abc() # should return 'a' on this first call
abc() # should return 'b' on this second call
abc() # should return 'c' on this third call
abc() # should return 'a' again on this fourth call

Different loopers should not affect each other, so be wary of unmanaged 
global state.

requirements:
    - keeps track of which character to return
    - loops back around when string is finished
    - needs to keep track of its own state

problems:
    - state mgmt in callable
    - getting successive characters from a string

"""

from collections.abc import Callable

S_IDX = dict()

def make_looper(string: str) -> Callable:
    S_IDX[string] = 0

    def looper():
        global S_IDX
        idx = S_IDX[string]
        s = string[idx]

        if S_IDX[string] >= len(string) - 1:
            S_IDX[string] = 0
        else:
            S_IDX[string] = S_IDX[string] + 1

        return s
    
    return looper

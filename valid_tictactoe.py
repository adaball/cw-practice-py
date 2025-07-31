"""https://www.codewars.com/kata/68582183cf16719a5ba943df"""

"""
You will be given a 3x3 list of characters (see Initial Solution and 
Sample Tests for the particular encoding used in your language) 
representing a Tic Tac Toe game board, with the following specifications:

    'X' is a square occupied by player X,
    'O' is a square occupied by player O,
    '_' is a square not occupied by either player.

Given this board, you need to determine whether this board represents 
a position that is reachable through normal play, and return a boolean 
value: true (if the condition is satisfied) and false otherwise.


Validation rules:
    - 'X' should always be the first player to move.
    - During one move, a player must occupy one extra square.
    - If a player manages to occupy 3 squares in a row (horizontally, vertically or diagonally), the game is immediately over and no further moves can be made; that player wins and is declared victorious (such a game is valid).
    - If all squares are occupied and neither player managed to get 3 in a row, the game ends in a draw (which is valid).
    - Games where not all squares are occupied and neither player got 3 in a row are considered valid.

Special case: This board (and similar ones where 'X' has two three-in-a-rows 
but the position can be reached):

X X X
O O X
O O X

when are games invalid?
    - more O's than X's
    - both O's and X's have three-in-a-rows

X
OOO
XXX


test cases:
        (
            (
                ('X', 'O', 'X'),
                ('X', 'O', 'X'),
                ('O', 'X', 'O'),
            ),
            True
        ),
        (
            (
                ('O', 'O', 'O'),
                ('X', 'X', 'X'),
                ('_', '_', 'X'),
            ),
            False
        ),
        (
            (
                ('X', 'X', 'O'),
                ('O', 'O', 'X'),
                ('X', 'O', 'O'),
            ),
            False
        ),
        (
            (
                ('X', 'X', 'X'),
                ('O', 'O', 'X'),
                ('O', 'O', 'X'),
            ),
            True
        ),


cnt = dict()
for row in board:
    for col in row:
        cnt[col] = cnt.get(col, 0) + 1

if cnt["O"] > cnt["X"]:
    valid = False

0,0 0,1 0,2 -> top row
1,0 1,1 1,2 -> mid row
2,0 2,1 2,2 -> bottom row
0,0 1,0 2,0 -> left col
0,1 1,1 2,1 -> middle col
0,2 1,2 2,2 -> right col
0,0 1,1 2,2 -> top-left diag
2,0 1,1 0,2 -> bottom-left diag

get_sq(board, coords):
    return board[coords[0], coords[1]]


threes = dict()
for a, b, c in coords:
   vals = [get_sq(board, a), get_sq(board, b), get_sq(board, c)] 
   all_o = all([True for v in vals if val == "O"])
   all_x = all([True for v in vals if val == "X"])

   if all_o:
     threes["O"] = threes.get("O", 0) + 1
   elif all_x:
     threes["X"] = threes.get("X", 0) + 1

special case is that if there is 2 three in a rows for one type and 0 for the
other, that's technically valid
otherwise there should only be <= 1 for both types
"""

possible_three_coords = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((2, 0), (1, 1), (0, 2)),
)

sample_board = (("X", "X", "X"), ("O", "O", "X"), ("O", "O", "X"))


def get_sq(board, coords):
    return board[coords[0]][coords[1]]


def check_for_threes(board):
    threes = dict()

    for a, b, c in possible_three_coords:
        vals = [get_sq(board, a), get_sq(board, b), get_sq(board, c)]

        all_o = all([True if v == "O" else False for v in vals])
        all_x = all([True if v == "X" else False for v in vals])

        if all_o:
            threes["O"] = threes.get("O", 0) + 1
        elif all_x:
            threes["X"] = threes.get("X", 0) + 1

    return threes


def is_valid_position(board: tuple[tuple[str, ...], ...]) -> bool:
    d = check_for_threes(sample_board)
    print(d)

    return False

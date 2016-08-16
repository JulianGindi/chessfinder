# Chess Move Finder!!

## Inputs

The main function `get_possible_moves` takes two inputs:

A board in the following format...

```
TEST_BOARD = [
    [0, 8, 9, 0, 12, 9, 8, 10],
    [7, 7, 7, 7, 7,  7, 0, 7],
    [0, 0, 10,0, 0,  0, 0, 0],
    [0, 0, 0, 11,0,  0, 0, 0],
    [0, 0, 0, 0, 0,  0, 7, 0],
    [0, 0, 0, 1, 3,  1, 0, 0],
    [1, 1, 1, 0, 1,  0, 1, 1],
    [4, 2, 0, 5, 6,  3, 2, 4]
]
```

...and the current player's turn indicated by a string `'white'` or `'black'`

## Output

Output is a mapping between locations on the board - `(2, 2)` - for example, and all the possible moves that piece can make.

Example:

`(0, 1): [(2, 0)]`

## Piece number to piece type chart

0: Empty

1: White Pawn

2: White Knight

3: White Bishop

4: White Rook

5: White Queen

6: White King

7: Black Pawn

8: Black Knight

9: Black Bishop

10: Black Rook

11: Black Queen

12: Black King

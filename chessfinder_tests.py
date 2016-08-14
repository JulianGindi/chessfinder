# Chess Tests
import unittest

from chessfinder import *

TEST_BOARD = [
    [0,8,9,11,12,9,8,10],
    [7,7,7,7,7,7,7,7],
    [0,0,10,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,3,0,0,0],
    [1,1,1,0,1,1,1,1],
    [4,2,0,5,6,3,2,4]
]

class TestChessFinder(unittest.TestCase):


    def test_return_piece_at_location(self):
        expected = ChessPiece.BBishop
        self.assertEqual(return_piece_at_location((0, 2), TEST_BOARD), expected)

    def test_black_pawn_movement(self):
        expected = (2, 0)
        piece_index = (1, 0)
        pawn_color = return_piece_at_location(piece_index, TEST_BOARD)
        self.assertEqual(pawn(pawn_color)(piece_index), expected)

    def test_white_pawn_movement(self):
        expected = (5, 0)
        piece_index = (6, 0)
        pawn_color = return_piece_at_location(piece_index, TEST_BOARD)
        self.assertEqual(pawn(pawn_color)(piece_index), expected)

    def test_rook_movement(self):
        expected = [(0, 2), (1, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2),
                    (2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)]
        piece_index = (2, 2)
        self.assertEqual(rook()(piece_index), expected)

    def test_bishop_movement(self):
        expected = [(7, 2), (6, 3), (4, 5), (3, 6), (2, 7)]
        piece_index = (5, 4)
        self.assertEqual(bishop()(piece_index), expected)

if __name__ == '__main__':
    unittest.main()

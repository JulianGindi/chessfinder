# Chess Tests
import unittest

from chessfinder import *

TEST_BOARD = [
    [10,8,9,11,12,9,8,10],
    [7,7,7,7,7,7,7,7],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1],
    [4,2,3,5,6,3,2,4]
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

    def test_black_rook_movement(self):
        expected = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
        piece_index = (0, 0)
        pawn_color = return_piece_at_location(piece_index, TEST_BOARD)
        self.assertEqual(rook(pawn_color)(piece_index), expected)

    def test_white_rook_movement(self):
        expected = [(6, 0), (5, 0), (4, 0), (3, 0), (2, 0), (1, 0), (0, 0)]
        piece_index = (7, 0)
        pawn_color = return_piece_at_location(piece_index, TEST_BOARD)
        self.assertEqual(rook(pawn_color)(piece_index), expected)

if __name__ == '__main__':
    unittest.main()

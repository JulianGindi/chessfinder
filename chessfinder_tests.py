# Chess Tests
import unittest

from chessfinder import *

TEST_BOARD = [
    #0  1  2  3  4   5  6  7
    [0, 8, 9, 0, 12, 9, 8, 10], # 0
    [7, 7, 7, 7, 7,  7, 7, 7],  # 1
    [0, 0, 10,0, 0,  0, 0, 0],  # 2
    [0, 0, 0, 11,0,  0, 0, 0],  # 3
    [0, 0, 0, 0, 0,  0, 0, 0],  # 4
    [0, 0, 0, 1, 3,  1, 0, 0],  # 5
    [1, 1, 1, 0, 1,  0, 1, 1],  # 6
    [4, 2, 0, 5, 6,  3, 2, 4]   # 7
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
        self.assertCountEqual(rook()(piece_index), expected)

    def test_bishop_movement(self):
        expected = [(7, 2), (6, 3), (4, 5), (3, 6), (2, 7),
                    (7, 6), (6, 5), (4, 3), (3, 2), (2, 1), (1, 0)]
        piece_index = (5, 4)
        self.assertCountEqual(bishop()(piece_index), expected)

    def test_queen_movement(self):
        expected = [(2, 3), (1, 3), (0, 3), (3, 0), (3, 1), (3, 2), (3, 4),
                    (3, 5), (3, 6), (3, 7), (4, 2), (5, 1), (6, 0), (2, 4),
                    (1, 5), (0, 6), (2, 2), (1, 1), (0, 0), (4, 4), (5, 5),
                    (6, 6), (7, 7), (4, 3), (5, 3), (6, 3), (7, 3)]
        piece_index = (3, 3)
        self.assertCountEqual(queen()(piece_index), expected)

    def test_king_movement(self):
        expected = [(7, 3), (7, 5), (6, 4), (6, 3), (6, 5)]
        piece_index = (7, 4)
        self.assertCountEqual(king()(piece_index), expected)

if __name__ == '__main__':
    unittest.main()

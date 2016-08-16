# Chess Tests
import unittest

from chessfinder import *

# Board format will be a multidimensional array
TEST_BOARD = [
    #0  1  2  3  4   5  6  7
    [0, 8, 9, 0, 12, 9, 8, 10], # 0
    [7, 7, 7, 7, 7,  7, 0, 7],  # 1
    [0, 0, 10,0, 0,  0, 0, 0],  # 2
    [0, 0, 0, 11,0,  0, 0, 0],  # 3
    [0, 0, 0, 0, 0,  0, 7, 0],  # 4
    [0, 0, 0, 1, 3,  1, 0, 0],  # 5
    [1, 1, 1, 0, 1,  0, 1, 1],  # 6
    [4, 2, 0, 5, 6,  3, 2, 4]   # 7
]

class TestChessFinder(unittest.TestCase):

    def test_return_piece_at_location(self):
        expected = ChessPiece.BBishop
        self.assertEqual(return_piece_at_location((0, 2), TEST_BOARD), expected)

    def test_black_pawn_movement(self):
        expected = [(2, 0), (3, 0)]
        piece_index = (1, 0)
        pawn_color = return_piece_at_location(piece_index, TEST_BOARD)
        self.assertCountEqual(pawn(pawn_color, piece_index, TEST_BOARD), expected)

    def test_white_pawn_movement(self):
        expected = [(4, 5), (4, 6)]
        piece_index = (5, 5)
        pawn_color = return_piece_at_location(piece_index, TEST_BOARD)
        self.assertCountEqual(pawn(pawn_color, piece_index, TEST_BOARD), expected)

    def test_rook_movement(self):
        expected = [(3, 2), (4, 2), (5, 2), (6, 2),
                    (2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)]
        piece_index = (2, 2)
        self.assertCountEqual(rook(piece_index, TEST_BOARD), expected)

    def test_knight_movement(self):
        expected = [(5, 7)]
        piece_index = (7, 6)
        self.assertCountEqual(knight(piece_index, TEST_BOARD), expected)

    def test_bishop_movement(self):
        expected = [(7, 2), (6, 3), (4, 5), (3, 6), (2, 7),
                    (6, 5), (4, 3), (3, 2), (2, 1), (1, 0)]
        piece_index = (5, 4)
        self.assertCountEqual(bishop(piece_index, TEST_BOARD), expected)

    def test_queen_movement(self):
        expected = [(2, 3), (3, 0), (3, 1), (3, 2), (3, 4),
                    (3, 5), (3, 6), (3, 7), (4, 2), (5, 1), (2, 4),
                    (4, 4), (5, 5), (4, 3), (5, 3), (6, 0)]
        piece_index = (3, 3)
        self.assertCountEqual(queen(piece_index, TEST_BOARD), expected)

    def test_king_movement(self):
        expected = [(6, 3), (6, 5)]
        piece_index = (7, 4)
        self.assertCountEqual(king(piece_index, TEST_BOARD), expected)

    def test_get_possible_moves(self):
        get_possible_moves(TEST_BOARD, 'white')

if __name__ == '__main__':
    unittest.main()

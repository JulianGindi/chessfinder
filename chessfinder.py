# ChessFinder
from typing import Tuple, List

# Custom type to represent a chesspiece index
BoardIndex = Tuple[int,int]
Board = List[List[str]]

BOARD_SIZE = 8

class ChessPiece:
        WPawn, WKnight, WBishop, WRook, WQueen, WKing, \
        BPawn, BKnight, BBishop, BRook, BQueen, BKing = range(1,13)


def pawn(piece_color: ChessPiece):
    if piece_color is ChessPiece.BPawn:
        return lambda x: (x[0] + 1, x[1])
    elif piece_color is ChessPiece.WPawn:
        return lambda x: (x[0] - 1, x[1])


def rook():
    def f(piece_index):
        v_moves = map(lambda x: (piece_index[0] + x, piece_index[1]), range(-BOARD_SIZE, BOARD_SIZE, 1))
        h_moves = map(lambda x: (piece_index[0], piece_index[1] + x), range(-BOARD_SIZE, BOARD_SIZE, 1))
        v_moves = filter_invalid_moves(v_moves, piece_index)
        h_moves = filter_invalid_moves(h_moves, piece_index)
        return list(v_moves) + list(h_moves)
    return f


def bishop():
    def f(piece_index):
        moves_a = map(lambda x: (piece_index[0] - x, piece_index[1] + x), range(-BOARD_SIZE, BOARD_SIZE, 1))
        moves_b = map(lambda x: (piece_index[0] - x, piece_index[1] - x), range(-BOARD_SIZE, BOARD_SIZE, 1))
        moves_a = filter_invalid_moves(moves_a, piece_index)
        moves_b = filter_invalid_moves(moves_b, piece_index)
        return moves_a + moves_b
    return f

def filter_invalid_moves(moves, pos):
    move_list = list(filter(lambda x: x[0] >= 0 and x[0] < BOARD_SIZE and x[1] >= 0 and x[1] < BOARD_SIZE, moves))
    move_list.remove(pos)
    return move_list


def is_legal_move(start: BoardIndex, end: BoardIndex, piece_type: ChessPiece) -> bool:
    pass


def return_piece_at_location(loc: BoardIndex, board: Board) -> ChessPiece:
    return board[loc[0]][loc[1]]


def spaces_to_next_piece(loc: BoardIndex, board: Board) -> Tuple[int, int]:
    pass

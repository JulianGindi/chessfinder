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

def rook(piece_color: ChessPiece):
    if piece_color is ChessPiece.BRook:
        def f(piece_index):
            v_moves = map(lambda x: (piece_index[0] + x, piece_index[1]), range(1, BOARD_SIZE))
            return list(v_moves)
        return f
    elif piece_color is ChessPiece.WRook:
        def f(piece_index):
            v_moves = map(lambda x: (piece_index[0] + x, piece_index[1]), range(-1, -BOARD_SIZE, -1))
            return list(v_moves)
        return f


def is_legal_move(start: BoardIndex, end: BoardIndex, piece_type: ChessPiece) -> bool:
    pass


def return_piece_at_location(loc: BoardIndex, board: Board) -> ChessPiece:
    return board[loc[0]][loc[1]]


def spaces_to_next_piece(loc: BoardIndex, board: Board) -> Tuple[int, int]:
    pass

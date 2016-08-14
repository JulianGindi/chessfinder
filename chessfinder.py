# ChessFinder
from typing import Tuple, List

# Custom type to represent a chesspiece index
BoardIndex = Tuple[int,int]
Board = List[List[str]]

BOARD_SIZE = 8

class ChessPiece:
        WPawn, WKnight, WBishop, WRook, WQueen, WKing, \
        BPawn, BKnight, BBishop, BRook, BQueen, BKing = range(1,13)


def king():
    def f(piece_index, board):
        movement = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        moves = add_movement_to_piece(piece_index, movement, board)
        return list(moves)
    return f


def pawn(piece_color: ChessPiece):
    def f(piece_index, board):
        movement = [(1, 0)]
        # If pawn is in starting file, it can move two spaces as well
        if piece_index[0] is 6 or piece_index[0] is 1:
            movement.append((2, 0))
        if piece_color is ChessPiece.BPawn:
            return map(lambda x: (piece_index[0] + x[0], piece_index[1]), movement)
        elif piece_color is ChessPiece.WPawn:
            return map(lambda x: (piece_index[0] - x[0], piece_index[1]), movement)
    return f


def rook():
    def f(piece_index, board):
        h_moves = walk(board, piece_index, 'horizontal')
        v_moves = walk(board, piece_index, 'vertical')
        return list(v_moves) + list(h_moves)
    return f


def bishop():
    def f(piece_index, board):
        moves_a = map(lambda x: (piece_index[0] - x, piece_index[1] + x),
                      range(-BOARD_SIZE, BOARD_SIZE, 1))
        moves_b = map(lambda x: (piece_index[0] - x, piece_index[1] - x),
                      range(-BOARD_SIZE, BOARD_SIZE, 1))
        moves_a = walk(board, piece_index, 'diagonalR')
        moves_b = walk(board, piece_index, 'diagonalL')
        return list(moves_a) + list(moves_b)
    return f


def knight():
    def f(piece_index, board):
        movement = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                    (0, 0), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        moves = add_movement_to_piece(piece_index, movement, board)
        return list(moves)
    return f


def queen():
    def f(piece_index, board):
        moves_a = rook()(piece_index, board)
        moves_b = bishop()(piece_index, board)
        return moves_a + moves_b
    return f


def add_movement_to_piece(piece_index, movement, board):
    m = map(lambda x: (piece_index[0] + x[0], piece_index[1] + x[1]), movement)
    m = filter_invalid_moves(m, piece_index, board)
    return m


# TODO: Need to figure out a way to handle pawn capture
def filter_invalid_moves(moves, piece_position, board):
    def is_valid_capture(x):
        piece_color = get_piece_color(piece_position, board)
        capture_color = get_piece_color(x, board)
        if capture_color is 'white' and piece_color is 'white':
            return False
        elif capture_color is 'black' and piece_color is 'black':
            return False
        return True

    move_list = list(filter(
        lambda x: x[0] >= 0 and x[0] < BOARD_SIZE and x[1] >= 0 and x[1] < BOARD_SIZE, moves
    ))
    move_list = list(filter(is_valid_capture, move_list))
    return move_list


def get_piece_color(piece_position, board):
    white_pieces = range(1, 7)
    black_pieces = range(7, 13)
    piece_type = return_piece_at_location(piece_position, board)
    if piece_type in white_pieces:
        return 'white'
    elif piece_type in black_pieces:
        return 'black'
    return None


def return_piece_at_location(loc: BoardIndex, board: Board) -> ChessPiece:
    return board[loc[0]][loc[1]]


def walk(board, piece_index, direction):
    move_list = []
    current_piece_index = piece_index
    piece_color = get_piece_color(piece_index, board)
    if direction is 'horizontal':
        i = 0
        # First we will check positive movement
        while i is 0:
            next_pos = (current_piece_index[0], current_piece_index[1] + 1)
            if next_pos[1] > 7:
                break
            i = return_piece_at_location(next_pos, board)
            current_piece_index = next_pos
            if get_piece_color(next_pos, board) is not piece_color:
                move_list.append(next_pos)

        i = 0
        current_piece_index = piece_index
        while i is 0:
            next_pos = (current_piece_index[0], current_piece_index[1] - 1)
            if next_pos[1] < 0:
                break
            i = return_piece_at_location(next_pos, board)
            current_piece_index = next_pos
            if get_piece_color(next_pos, board) is not piece_color:
                move_list.append(next_pos)
    elif direction is 'vertical':
        i = 0
        # First we will check positive movement
        while i is 0:
            next_pos = (current_piece_index[0] + 1, current_piece_index[1])
            if next_pos[0] > 7:
                break
            i = return_piece_at_location(next_pos, board)
            current_piece_index = next_pos
            if get_piece_color(next_pos, board) is not piece_color:
                move_list.append(next_pos)

        i = 0
        current_piece_index = piece_index
        while i is 0:
            next_pos = (current_piece_index[0] - 1, current_piece_index[1])
            if next_pos[0] < 0:
                break
            i = return_piece_at_location(next_pos, board)
            current_piece_index = next_pos
            if get_piece_color(next_pos, board) is not piece_color:
                move_list.append(next_pos)
    elif direction is 'diagonalR':
        i = 0
        # First we will check positive movement
        while i is 0:
            next_pos = (current_piece_index[0] + 1, current_piece_index[1] + 1)
            if next_pos[0] > 7 or next_pos[1] > 7:
                break
            i = return_piece_at_location(next_pos, board)
            current_piece_index = next_pos
            if get_piece_color(next_pos, board) is not piece_color:
                move_list.append(next_pos)

        i = 0
        current_piece_index = piece_index
        while i is 0:
            next_pos = (current_piece_index[0] - 1, current_piece_index[1] - 1)
            if next_pos[0] < 0 or next_pos[1] < 0:
                break
            i = return_piece_at_location(next_pos, board)
            current_piece_index = next_pos
            if get_piece_color(next_pos, board) is not piece_color:
                move_list.append(next_pos)
    elif direction is 'diagonalL':
        i = 0
        # First we will check positive movement
        while i is 0:
            next_pos = (current_piece_index[0] + 1, current_piece_index[1] - 1)
            if next_pos[0] > 7 or next_pos[1] > 7:
                break
            i = return_piece_at_location(next_pos, board)
            current_piece_index = next_pos
            if get_piece_color(next_pos, board) is not piece_color:
                move_list.append(next_pos)

        i = 0
        current_piece_index = piece_index
        while i is 0:
            next_pos = (current_piece_index[0] - 1, current_piece_index[1] + 1)
            if next_pos[0] < 0 or next_pos[1] < 0:
                break
            i = return_piece_at_location(next_pos, board)
            current_piece_index = next_pos
            if get_piece_color(next_pos, board) is not piece_color:
                move_list.append(next_pos)

    return move_list

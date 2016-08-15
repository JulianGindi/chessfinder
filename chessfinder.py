# ChessFinder
import operator

BOARD_SIZE = 8

# Using this class as a simple enum matching human-readable names with
# easier to work with ints
class ChessPiece:
    WPawn, WKnight, WBishop, WRook, WQueen, WKing, \
            BPawn, BKnight, BBishop, BRook, BQueen, BKing = range(1, 13)


def king():
    def f(piece_index, board):
        movement = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        moves = add_movement_to_piece(piece_index, movement, board)
        return list(moves)
    return f


# TODO: Refactor
def pawn(piece_color):
    def f(piece_index, board):
        movement = [(1, 0)]
        # If pawn is in starting file, it can move two spaces as well
        if piece_index[0] is 6 or piece_index[0] is 1:
            movement.append((2, 0))
        if piece_color is ChessPiece.BPawn:
            if get_piece_color(add_board_index(piece_index, (1, 1)), board) is not 'black' and \
               return_piece_at_location(add_board_index(piece_index, (1, 1)), board) is not 0:
                movement.append((1, 1))
            elif get_piece_color(add_board_index(piece_index, (1, -1)), board) is not 'black' and \
                    return_piece_at_location(add_board_index(piece_index, (1, -1)), board) is not 0:
                movement.append((1, -1))
            return map(lambda x: (piece_index[0] + x[0], piece_index[1] + x[1]), movement)
        elif piece_color is ChessPiece.WPawn:
            if get_piece_color(add_board_index(piece_index, (-1, 1)), board) is not 'white' and \
               return_piece_at_location(add_board_index(piece_index, (-1, 1)), board) is not 0:
                movement.append((1, 1))
            if get_piece_color(add_board_index(piece_index, (-1, -1)), board) is not 'white' and \
               return_piece_at_location(add_board_index(piece_index, (-1, -1)), board) is not 0:
                movement.append((1, -1))
            return map(lambda x: (piece_index[0] - x[0], piece_index[1] + x[1]), movement)
    return f


def rook():
    def f(piece_index, board):
        h_moves = walk(board, piece_index, 'horizontal')
        v_moves = walk(board, piece_index, 'vertical')
        return list(v_moves) + list(h_moves)
    return f


def bishop():
    def f(piece_index, board):
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
        #import pdb; pdb.set_trace()
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


def return_piece_at_location(loc, board):
    return board[loc[0]][loc[1]]


def add_board_index(index, movement):
    return tuple(map(operator.add, index, movement))


def out_of_bounds(piece_index):
    return piece_index[0] > 7 or piece_index[0] < 0 \
            or piece_index[1] > 7 or piece_index[1] < 0


def walk_recursive(piece_index, original_piece, movement, board, move_list, first_loop=False):
    original_piece_color = get_piece_color(original_piece, board)
    next_pos = add_board_index(piece_index, movement)
    if out_of_bounds(piece_index):
        return move_list
    if return_piece_at_location(piece_index, board) is 0:
        move_list.append(piece_index)
    if get_piece_color(piece_index, board) is not original_piece_color and return_piece_at_location(piece_index, board) is not 0:
        move_list.append(piece_index)
        return move_list
    if get_piece_color(piece_index, board) is original_piece_color and not first_loop:
        return move_list
    return walk_recursive(next_pos, original_piece, movement, board, move_list)


def walk(board, piece_index, direction):
    move_list = []
    current_piece_index = piece_index
    if direction is 'horizontal':
        move_list = walk_recursive(piece_index, piece_index, (0, 1), board, move_list, True)
        move_list = walk_recursive(piece_index, piece_index, (0, -1), board, move_list, True)
    elif direction is 'vertical':
        move_list = walk_recursive(piece_index, piece_index, (1, 0), board, move_list, True)
        move_list = walk_recursive(piece_index, piece_index, (-1, 0), board, move_list, True)
    elif direction is 'diagonalR':
        move_list = walk_recursive(piece_index, piece_index, (1, 1), board, move_list, True)
        move_list = walk_recursive(piece_index, piece_index, (-1, -1), board, move_list, True)
    elif direction is 'diagonalL':
        move_list = walk_recursive(piece_index, piece_index, (1, -1), board, move_list, True)
        move_list = walk_recursive(piece_index, piece_index, (-1, 1), board, move_list, True)
    return move_list


# Our Main Function
def get_possible_moves(board, color):
    for row in board:
        for piece in row:
            pass

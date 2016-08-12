# ChessFinder

# Custom type to represent a chesspiece index
BoardIndex = List[int,int]


class ChessPiece:
        Pawn, Knight, Bishop, Rook, Queen, King = range(6)


def is_legal_move(start: BoardIndex, end: BoardIndex, piece_type: ChessPiece) -> bool:
    pass


def return_pieace_at_location(loc: BoardIndex) -> ChessPiece:
    pass

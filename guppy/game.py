# from move_generation import Move
from ui import display_board, identify_piece

def get_coordinate_dictionary():
    coordinate_dict = {}
    for i in range(64):
        rank = i // 8
        file = i % 8
        ranks = "12345678"
        files = "abcdefgh"
        coordinate_dict[i] = f"{files[file]}{ranks[rank]}"
    return coordinate_dict


class ChessGame:

    COORDINATES = get_coordinate_dictionary()
    INDICES = {v: k for k, v in COORDINATES.items()}
    BITBOARDS = {
        "wp": "white_pawns",
        "wR": "white_rooks",
        "wN": "white_knights",
        "wB": "white_bishops",
        "wQ": "white_queens",
        "wK": "white_king",
        "bp": "black_pawns",
        "bR": "black_rooks",
        "bN": "black_knights",
        "bB": "black_bishops",
        "bQ": "black_queens",
        "bK": "black_king"
    }

    def __init__(self):
        self.setup_board()


    def setup_board(self):
        self.black_pawns = 0x00FF000000000000 
        self.black_rooks = (1 << 56) | (1 << 63)
        self.black_knights = (1 << 57) | (1 << 62) 
        self.black_bishops = (1 << 58) | (1 << 61)
        self.black_queens = (1 << 59)
        self.black_king = (1 << 60)

        self.white_pawns = 0x000000000000FF00
        self.white_rooks = (1 << 0) | (1 << 7)
        self.white_knights = (1 << 1) | (1 << 6)
        self.white_bishops = (1 << 2) | (1 << 5)
        self.white_queens = (1 << 3)
        self.white_king = (1 << 4)


    def get_empty_squares(self): # NEEDS WORK...?
        occupied_squares = (
            self.white_pawns | self.black_pawns |
            self.white_rooks | self.black_rooks |
            self.white_knights | self.black_knights |
            self.white_bishops | self.black_bishops |
            self.white_queens | self.black_queens |
            self.white_king | self.black_king
        )
        empty_squares = ~occupied_squares
        return empty_squares
    
    def get_legal_moves(self, piece, origin):
        pass


    def move(self, move):

        # Change this to algebraic notation when I figure out move option generation
        destination = move.pop()
        if move:
            origin = move.pop()

        if isinstance(origin, str):
            origin = self.INDICES[origin]
        if isinstance(destination, str):
            destination = self.INDICES[destination]
        
        piece = identify_piece(self, origin)
        current_bb = getattr(self, self.BITBOARDS[piece])
        updated_bb = (current_bb & ~(1 << origin)) | (1 << destination)
        setattr(self, self.BITBOARDS[piece], updated_bb)


def main():
    chess = ChessGame()

    print(bin(chess.get_empty_squares())[2:].zfill(64))
    for m in [["e2", "e4"], ["e7", "e5"], ["g1", "f3"], ["b8", "c6"], ["f1", "b5"]]:
        chess.move(m)


    display_board(chess)

    print(bin(chess.get_empty_squares())[2:].zfill(64))

if __name__ == "__main__":
    main()
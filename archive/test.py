# Define constants for the pieces
EMPTY = 0
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

# Define constants for the sides
WHITE = 0
BLACK = 1

# Initialize the bitboards for each piece type
class Bitboard:
    def __init__(self):
        # Bitboards for each piece type for both colors
        self.bitboards = {
            WHITE: {
                PAWN: 0x000000000000FF00,
                KNIGHT: 0x0000000000000042,
                BISHOP: 0x0000000000000024,
                ROOK: 0x0000000000000081,
                QUEEN: 0x0000000000000008,
                KING: 0x0000000000000010,
            },
            BLACK: {
                PAWN: 0x00FF000000000000,
                KNIGHT: 0x4200000000000000,
                BISHOP: 0x2400000000000000,
                ROOK: 0x8100000000000000,
                QUEEN: 0x0800000000000000,
                KING: 0x1000000000000000,
            }
        }

    def print_bitboard(self, bitboard):
        for rank in range(8):
            for file in range(8):
                square = rank * 8 + file
                print('1' if (bitboard >> square) & 1 else '.', end=' ')
            print()
        print()

# Initialize the board
board = Bitboard()
board.print_bitboard(board.bitboards[WHITE][PAWN])
board.print_bitboard(board.bitboards[BLACK][PAWN])
print(board.bitboards)
 
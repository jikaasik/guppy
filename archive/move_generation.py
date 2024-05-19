"""
Bitwise movement

pawns: +/-8 or +/-16; +/-7 or +/-9 when capturing
knights: +/- [6, 15, 17, 10]
bishops: +/- multiples of 9, +/- multiples of 7
rooks: +/- multiples of 1 (max 7); +/- multiples of 8
queens: +/- multiples of 1, 7, 8, 9
kings: +/- [1, 7, 8, 9]

"""

"""
Edge constraints

knight: sum(abs(change_row + change_column)) == 3
bishop: abs(change_row + change_column) % 2 == 0
rook
queen


"""

# def build_lookup():
#     move_lookup = {}

#     for i in range(64):
#         row = i // 8
#         column = i % 8
#         for p in ["bishop"]:
#             moves = []
#             for r in range(1, row+1)
#             # maybe the minimum of row and column should determine range?
def get_pawn_moves(self, bitboard, white_turn):
    moves = []
    if white_turn:
        for square in range(64):
            if (bitboard >> square) & 1:
                if 8 <= square <= 15:
                    moves.append((square, square + 8))
                    moves.append((square, square + 16))
                else:
                    moves.append((square, square + 8))
    else:
        for square in range(64):
            if (bitboard >> square) & 1:
                if 48 <= square <= 55:
                    moves.append((square, square - 8))
                    moves.append((square, square - 16))
                else:
                    moves.append((square, square - 8))
    return moves
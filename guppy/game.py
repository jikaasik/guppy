from board import Bitboard
from moves import MoveGenerator
import random

board = Bitboard()
moves = MoveGenerator()

# for m in [["P", ["e2", "e4"]], ["p", ["e7", "e5"]], ["N", ["g1", "f3"]], ["n", ["b8", "c6"]]]:
#     piece = m[0]
#     move = m[1]
#     board.make_move(piece, move)



# white_turn = True
# for i in range(7):
#     piece = "P" if white_turn else "p"
#     pawn_moves = moves.get_pawn_moves(board.bitboards[piece], white_turn)
#     board.make_move(piece, pawn_moves[0])

#     white_turn = not white_turn

# board.print_board()

# white_turn = True
# for i in range(2):
#     piece = "N" if white_turn else "n"
#     knight_moves = moves.get_knight_moves(board.bitboards[piece], white_turn)
#     print(f"{piece} moves are:\n")
#     for move in knight_moves:
#         try:
#             print(board.COORDINATES[move[0]], "to", board.COORDINATES[move[1]])
#         except:
#             print(move)
        
#     # board.make_move(piece, knight_moves[0])

white_turn = True
for i in range(26):
    valid_moves = moves.get_moves(board.bitboards, white_turn)
    selected_move = random.choice(valid_moves)
    print(selected_move)
    piece = "P" if white_turn else "p"
    print(piece)
    board.make_move(piece, selected_move)
    print(white_turn)
    board.print_board()
    white_turn = not white_turn


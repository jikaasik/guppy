from attacks import init_bishop_attacks, init_rook_attacks
import pdb
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

# for i in range(12):
#     white_turn = board.game_state['white_turn']
#     color = "White" if white_turn else "Black"
#     print(color)
#     valid_moves = moves.get_moves(board.bitboards, board.game_state)
#     capture_moves = [n for n in valid_moves if board.identify_occupant(n[1])]

#     if capture_moves:
#         selected_move = random.choice(capture_moves)
#     else:
#         selected_move = random.choice(valid_moves)

#     piece = board.identify_occupant(selected_move[0])
#     board.make_move(piece, selected_move)
#     board.print_board()


# for i in [0, 1, 2, 6, 7, 8, 9, 14, 15, 28, 48, 49, 54, 55, 56, 62, 63]:
#     # for i in [28]:
#     print(f"King attacks for {moves.COORDINATES[i]}")
#     board.print_board(moves.king_attack_mask[i])


square = moves.INDICES['e4']
piece = (1 << moves.INDICES['d5'])
test_rook = init_rook_attacks(square, piece)
test_bishop = init_bishop_attacks(square, piece)
board.print_board(test_rook)

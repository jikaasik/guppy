class MoveGenerator:

    NOT_A_FILE = 0xFEFEFEFEFEFEFEFE
    NOT_B_FILE = 0xFDFDFDFDFDFDFDFD
    NOT_AB_FILE = 0xFCFCFCFCFCFCFCFC
    NOT_G_FILE = 0x7F7F7F7F7F7F7F7F
    NOT_H_FILE = 0xBFBFBFBFBFBFBFBF
    NOT_GH_FILE = 0x3F3F3F3F3F3F3F3F
    # NOT_1_RANK = 0xFFFFFFFFFFFFFF00
    # NOT_2_RANK = 0xFFFFFFFFFFFF00FF
    # NOT_12_RANK = 0xFFFFFFFFFFFF0000
    # NOT_7_RANK = 0xFF00FFFFFFFFFFFF
    # NOT_8_RANK = 0x00FFFFFFFFFFFFFF
    # NOT_78_RANK = 0x0000FFFFFFFFFFFF

    def __init__(self):
        pass
    
    def get_moves(self):
        print("yipee")

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



    # def get_knight_moves(self, bitboard, color):
    #     moves = []
    #     for square in range(64):
    #         if (bitboard >> square) & 1:
    #             moves.append((square, (square))

    #     return moves


    def get_rook_moves(self, bitboard, color):
        pass


    def get_bishop_moves(self, bitboard, color):
        pass


    def get_queen_moves(self, bitboard, color):
        pass


    def get_king_moves(self, bitboard, color):
        pass


    def validate_move_legal(self, move, color):
        pass

    
    def is_in_check(self):
        pass


    def move(self):
        pass

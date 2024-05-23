NOT_A_FILE = 0xFEFEFEFEFEFEFEFE
NOT_B_FILE = 0xFDFDFDFDFDFDFDFD
NOT_AB_FILE = 0xFCFCFCFCFCFCFCFC
NOT_G_FILE = 0xBFBFBFBFBFBFBFBF
NOT_H_FILE = 0x7F7F7F7F7F7F7F7F
NOT_GH_FILE = 0x3F3F3F3F3F3F3F3F


def init_pawn_attacks() -> dict:
    pawn_attacks = {
        'white': dict(),
        'black': dict()
    }

    for white_turn in [True, False]:
        for i in range(64):
            attacks = 0
            bitboard = (1 << i)

            if not white_turn:
                if bitboard & NOT_H_FILE:
                    attacks |= (bitboard >> 7)
                if bitboard & NOT_A_FILE:
                    attacks |= (bitboard >> 9)
                pawn_attacks['black'][i] = attacks
            else:
                if bitboard & NOT_A_FILE:
                    attacks |= (bitboard << 7)
                if bitboard & NOT_H_FILE:
                    attacks |= (bitboard << 9)
                pawn_attacks['white'][i] = attacks

    return pawn_attacks


def init_knight_attacks() -> dict:
    knight_attacks = None


def init_king_attacks() -> dict:
    king_attacks = None

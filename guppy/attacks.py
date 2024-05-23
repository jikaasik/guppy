NOT_A_FILE = 0xFEFEFEFEFEFEFEFE
NOT_B_FILE = 0xFDFDFDFDFDFDFDFD
NOT_AB_FILE = 0xFCFCFCFCFCFCFCFC
NOT_G_FILE = 0xBFBFBFBFBFBFBFBF
NOT_H_FILE = 0x7F7F7F7F7F7F7F7F
NOT_GH_FILE = 0x3F3F3F3F3F3F3F3F


def init_pawn_attacks() -> dict:
    """Returns a dict of pawn attack masks (1 per index)"""
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
    """Returns a dict of knight attack masks (1 per index)"""
    knight_attacks = dict()
    for i in range(64):
        attacks = 0
        bitboard = (1 << i)

        if (bitboard << 17) & NOT_A_FILE:
            attacks |= (bitboard << 17)
        if (bitboard << 10) & NOT_AB_FILE:
            attacks |= (bitboard << 10)
        if (bitboard >> 6) & NOT_AB_FILE:
            attacks |= (bitboard >> 6)
        if (bitboard >> 15) & NOT_A_FILE:
            attacks |= (bitboard >> 15)
        if (bitboard << 15) & NOT_H_FILE:
            attacks |= (bitboard << 15)
        if (bitboard << 6) & NOT_GH_FILE:
            attacks |= (bitboard << 6)
        if (bitboard >> 10) & NOT_GH_FILE:
            attacks |= (bitboard >> 10)
        if (bitboard >> 17) & NOT_H_FILE:
            attacks |= (bitboard >> 17)
        knight_attacks[i] = attacks

    return knight_attacks


def init_king_attacks() -> dict:
    """Returns a dict of king attack masks (1 per index)"""
    king_attacks = None

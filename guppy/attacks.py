NOT_A_FILE = 0xFEFEFEFEFEFEFEFE
NOT_B_FILE = 0xFDFDFDFDFDFDFDFD
NOT_AB_FILE = 0xFCFCFCFCFCFCFCFC
NOT_G_FILE = 0xBFBFBFBFBFBFBFBF
NOT_H_FILE = 0x7F7F7F7F7F7F7F7F
NOT_GH_FILE = 0x3F3F3F3F3F3F3F3F


def get_rank_file(square) -> tuple:
    """Returns the rank and file of a square index."""

    r = int(square / 8)
    f = int(square % 8)
    return r, f


def init_pawn_attacks() -> dict:
    """Returns a dict of pawn attack masks"""

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
    """Returns a dict of knight attack masks"""

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
    """Returns a dict of king attack masks"""

    king_attacks = dict()
    for i in range(64):
        attacks = 0
        bitboard = (1 << i)

        if (bitboard >> 8):
            attacks |= (bitboard >> 8)
        if (bitboard << 8):
            attacks |= (bitboard << 8)
        if ((bitboard >> 9) & NOT_H_FILE):
            attacks |= (bitboard >> 9)
        if ((bitboard << 9) & NOT_A_FILE):
            attacks |= (bitboard << 9)
        if ((bitboard >> 7) & NOT_A_FILE):
            attacks |= (bitboard >> 7)
        if ((bitboard << 7) & NOT_H_FILE):
            attacks |= (bitboard << 7)
        if ((bitboard >> 1) & NOT_H_FILE):
            attacks |= (bitboard >> 1)
        if ((bitboard << 1) & NOT_A_FILE):
            attacks |= (bitboard << 1)
        king_attacks[i] = attacks

    return king_attacks


def init_bishop_attacks(square, piece=0) -> int:
    attacks = 0

    r, f = get_rank_file(square)
    while r < 6 and f < 6:
        r += 1
        f += 1
        target = (1 << (r * 8 + f))
        attacks |= target
        if target & piece:
            break

    r, f = get_rank_file(square)
    while r < 6 and f > 1:
        r += 1
        f -= 1
        target = (1 << (r * 8 + f))
        attacks |= target
        if target & piece:
            break

    r, f = get_rank_file(square)
    while r > 1 and f > 1:
        r -= 1
        f -= 1
        target = (1 << (r * 8 + f))
        attacks |= target
        if target & piece:
            break

    r, f = get_rank_file(square)
    while r > 1 and f < 6:
        r -= 1
        f += 1
        target = (1 << (r * 8 + f))
        attacks |= target
        if target & piece:
            break

    return attacks


def init_rook_attacks(square, piece=0) -> int:
    attacks = 0

    r, f = get_rank_file(square)
    for i in range(f + 1, 7):
        target = (1 << (r * 8 + i))
        attacks |= target
        if target & piece:
            break

    for i in range(r + 1, 7):
        target = (1 << (i * 8 + f))
        attacks |= target
        if target & piece:
            break

    for i in range(f - 1, 0, -1):
        target = (1 << (r * 8 + i))
        attacks |= target
        if target & piece:
            break

    for i in range(r - 1, 0, -1):
        target = (1 << (i * 8 + f))
        attacks |= target
        if target & piece:
            break

    return attacks


bishop_bit_counts = {
    6, 5, 5, 5, 5, 5, 5, 6,
    5, 5, 5, 5, 5, 5, 5, 5,
    5, 5, 7, 7, 7, 7, 5, 5,
    5, 5, 7, 9, 9, 7, 5, 5,
    5, 5, 7, 9, 9, 7, 5, 5,
    5, 5, 7, 7, 7, 7, 5, 5,
    5, 5, 5, 5, 5, 5, 5, 5,
    6, 5, 5, 5, 5, 5, 5, 6
}

rook_bit_counts = {
    12, 11, 11, 11, 11, 11, 11, 12,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    11, 10, 10, 10, 10, 10, 10, 11,
    12, 11, 11, 11, 11, 11, 11, 12
}

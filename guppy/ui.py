ICONS = {
    'wp': '♟︎',
    'wN': '♞',
    'wB': '♝',
    'wR': '♜',
    'wQ': '♛',
    'wK': '♚',
    'bp': '♙',
    'bN': '♘',
    'bB': '♗',
    'bR': '♖',
    'bQ': '♕',
    'bK': '♔',
    '.': '.'
}


def display_board(game):
    print("  a b c d e f g h")
    for row in range(8):
        print(8 - row, end=' ')
        for col in range(8, 0, -1):
            square_index = abs(64 - (row * 8 + col))
            piece = identify_piece(game, square_index)
            piece_icon = ICONS[piece]
            print(piece_icon, end=' ')
        print()
    print()


def identify_piece(game, position):
    if isinstance(position, str):
        position = game.INDICES[position]

    if game.black_pawns & (1 << position):
        piece = "bp"
    elif game.white_pawns & (1 << position):
        piece = "wp"
    elif game.black_knights & (1 << position):
        piece = "bN"
    elif game.white_knights & (1 << position):
        piece = "wN"
    elif game.black_bishops & (1 << position):
        piece = "bB"
    elif game.white_bishops & (1 << position):
        piece = "wB"
    elif game.black_rooks & (1 << position):
        piece = "bR"
    elif game.white_rooks & (1 << position):
        piece = "wR"
    elif game.black_queens & (1 << position):
        piece = "bQ"
    elif game.white_queens & (1 << position):
        piece = "wQ"
    elif game.black_king & (1 << position):
        piece = "bK"
    elif game.white_king & (1 << position):
        piece = "wK"
    else:
        piece = "."
    
    return piece
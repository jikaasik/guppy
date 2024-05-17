ICONS = {
    'P': '♟︎',
    'N': '♞',
    'B': '♝',
    'R': '♜',
    'Q': '♛',
    'K': '♚',
    'p': '♙',
    'n': '♘',
    'b': '♗',
    'r': '♖',
    'q': '♕',
    'k': '♔',
    '.': '.'
}

def get_coordinate_dictionary():
    """Generates the algebraic notation coordinates for the index of each square."""

    coordinate_dict = {}
    for i in range(64):
        row = (i + 8) // 8
        column = i % 8
        columns = "abcdefgh"
        coordinate_dict[i] = f"{columns[column]}{row}"
    return coordinate_dict


class Bitboard:
    """A class that holds the current board state as a set of bitboards."""

    COORDINATES = get_coordinate_dictionary()
    INDICES = {v: k for k, v in COORDINATES.items()}

    def __init__(self):
        self.bitboards = {
            # White pieces
            'P': 0x000000000000FF00,
            'N': 0x0000000000000042,
            'B': 0x0000000000000024,
            'R': 0x0000000000000081,
            'Q': 0x0000000000000008,
            'K': 0x0000000000000010,

            # Black pieces
            'p': 0x00FF000000000000,
            'n': 0x4200000000000000,
            'b': 0x2400000000000000,
            'r': 0x8100000000000000,
            'q': 0x0800000000000000,
            'k': 0x1000000000000000
        }

    def print_board(self):
        """Prints the current game state."""

        for r in range(8):
            print(8 - r, end=' ')
            for f in range(8):
                square = 8 * r + f
                piece = None
                for k, v in self.bitboards.items():
                    if (self.bitboards[k] >> square) & 1:
                        piece = k
                print(ICONS[piece] if piece else '.', end=' ')
            print()
        print('  a b c d e f g h')


if __name__ == '__main__':
    board = Bitboard()
    board.print_board()
    print(Bitboard.COORDINATES[0])
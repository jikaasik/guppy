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


def get_coordinate_dictionary() -> tuple[list, dict]:
    """Generates the algebraic notation for the index of each square."""

    coordinate_list = []
    for i in range(64):
        row = (i + 8) // 8
        column = i % 8
        columns = 'abcdefgh'
        coordinate_list.append(f"{columns[column]}{row}")
    indices_dict = {coordinate_list[i]: i for i in range(64)}
    return coordinate_list, indices_dict


class Bitboard:
    """A class that holds the current board state as a set of bitboards."""

    COORDINATES, INDICES = get_coordinate_dictionary()

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
        self.game_state = {
            'white_turn': True,
            'castling_rights': {'K', 'Q', 'k', 'q'},
            'en_passant': '',
            'half_moves': 0,
            'move_count': 0
        }

    def make_move(self, piece: str, move: tuple[int, int]) -> None:

        origin, destination = move

        if isinstance(origin, str):
            origin = self.INDICES[origin]
        if isinstance(destination, str):
            destination = self.INDICES[destination]

        # Check legality of move

        # Update mover bitboard
        updated_bitboard = (self.bitboards[piece] & ~(
            1 << origin)) | (1 << destination)

        # Remove previous occupant from board, if captured
        occupant = self.identify_occupant(destination)
        if occupant:
            self.bitboards[occupant] = self.bitboards[occupant] & ~(1 << destination)
            print(f"{piece}x{self.COORDINATES[destination]}")
        else:
            print(f"{piece}{destination}")

        # Update bitboards
        self.bitboards[piece] = updated_bitboard

    def identify_occupant(self, index: int) -> str:
        """Returns the current occupant of a given bitboard index (if any)."""

        piece = None
        for k, v in self.bitboards.items():
            if (self.bitboards[k] >> index) & 1:
                piece = k
        return piece

    def parse_fen(self, fen: str) -> None:
        # Initialize bitboards
        piece_bitboards = dict()
        for piece in [n for n in 'PRNBQKprnbqk']:
            piece_bitboards[piece] = 0

        # Split FEN
        fen_parts = fen.split()
        piece_placement = fen_parts[0]
        fen_game_state = {
            'white_turn': True if fen_parts[1] == 'w' else False,
            'castling_rights': {fen_parts[2]}.difference({'-'}),
            'en_passant': fen_parts[3] if fen_parts[3] != '-' else '',
            'half_moves': int(fen_parts[4]),
            'move_count': int(fen_parts[5])
        }

        # Get piece placements
        rows = piece_placement.split('/')
        for rank_idx, row in enumerate(rows):
            file_idx = 0
            for char in row:
                if char.isdigit():
                    file_idx += int(char)
                else:
                    square = (7 - rank_idx) * 8 + file_idx
                    piece_bitboards[char] |= 1 << square
                    file_idx += 1

        setattr(self, 'bitboards', piece_bitboards)
        setattr(self, 'game_state', fen_game_state)

    def print_board(self, board: int = None):
        """Prints the current game state."""

        for r in range(7, -1, -1):
            print(r + 1, end=' ')
            for f in range(8):
                square = 8 * r + f
                if not board:
                    piece = self.identify_occupant(square)
                    print(ICONS[piece] if piece else '.', end=' ')
                else:
                    print(1 if (board >> square) & 1 else '.', end=' ')
            print()
        print('  a b c d e f g h \n')

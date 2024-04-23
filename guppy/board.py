def get_coordinate_dictionary():
    coordinate_dict = {}
    for i in range(64):
        row = (i + 8) // 8
        column = i % 8
        columns = "abcdefgh"
        coordinate_dict[i] = f"{columns[column]}{row}"
    return coordinate_dict


class Board:

    COORDINATES = get_coordinate_dictionary()
    INDICES = {v: k for k, v in COORDINATES.items()}
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


    def setup_board(self):
        self.black_pawns = 0x00FF000000000000 
        self.black_rooks = (1 << 56) | (1 << 63)
        self.black_knights = (1 << 57) | (1 << 62) 
        self.black_bishops = (1 << 58) | (1 << 61)
        self.black_queens = (1 << 59)
        self.black_king = (1 << 60)

        self.white_pawns = 0x000000000000FF00
        self.white_rooks = (1 << 0) | (1 << 7)
        self.white_knights = (1 << 1) | (1 << 6)
        self.white_bishops = (1 << 2) | (1 << 5)
        self.white_queens = (1 << 3)
        self.white_king = (1 << 4)

    
    def display_board(self):
        print("  a b c d e f g h")
        for row in range(8):
            print(8 - row, end=' ')
            for col in range(8, 0, -1):
                square_index = abs(64 - (row * 8 + col))
                piece = self.identify_piece(square_index)
                piece_icon = self.ICONS[piece]
                print(piece_icon, end=' ')
            print()  # Newline after each row
        print()  # Extra newline for better separation

    def identify_piece(self, position):
        if isinstance(position, str):
            position = self.INDICES[position]

        if self.black_pawns & (1 << position):
            piece = "bp"
        elif self.white_pawns & (1 << position):
            piece = "wp"
        elif self.black_knights & (1 << position):
            piece = "bN"
        elif self.white_knights & (1 << position):
            piece = "wN"
        elif self.black_bishops & (1 << position):
            piece = "bB"
        elif self.white_bishops & (1 << position):
            piece = "wB"
        elif self.black_rooks & (1 << position):
            piece = "bR"
        elif self.white_rooks & (1 << position):
            piece = "wR"
        elif self.black_queens & (1 << position):
            piece = "bQ"
        elif self.white_queens & (1 << position):
            piece = "wQ"
        elif self.black_king & (1 << position):
            piece = "bK"
        elif self.white_king & (1 << position):
            piece = "wK"
        else:
            piece = "."
        
        return piece
        
        



            

def main():
    chess = Board()
    chess.setup_board()
    chess.display_board()


if __name__ == "__main__":
    main()
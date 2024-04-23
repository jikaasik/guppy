class Chess:
    def __init__(self):
        self.white_pawns = 0
        self.black_pawns = 0
        self.white_knights = 0
        self.black_knights = 0
        self.white_bishops = 0
        self.black_bishops = 0
        self.white_rooks = 0
        self.black_rooks = 0
        self.white_queens = 0
        self.black_queens = 0
        self.white_king = 0
        self.black_king = 0

    
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
                piece_icon = '.'
                if self.black_pawns & (1 << square_index):
                    piece_icon = '♙'
                elif self.white_pawns & (1 << square_index):
                    piece_icon = '♟︎'
                elif self.black_knights & (1 << square_index):
                    piece_icon = '♘'
                elif self.white_knights & (1 << square_index):
                    piece_icon = '♞'
                elif self.black_bishops & (1 << square_index):
                    piece_icon = '♗'
                elif self.white_bishops & (1 << square_index):
                    piece_icon = '♝'
                elif self.black_rooks & (1 << square_index):
                    piece_icon = '♖'
                elif self.white_rooks & (1 << square_index):
                    piece_icon = '♜'
                elif self.black_queens & (1 << square_index):
                    piece_icon = '♕'
                elif self.white_queens & (1 << square_index):
                    piece_icon = '♛'
                elif self.black_king & (1 << square_index):
                    piece_icon = '♔'
                elif self.white_king & (1 << square_index):
                    piece_icon = '♚'
                print(piece_icon, end=' ')
            print()  # Newline after each row
        print()  # Extra newline for better separation
    

from board import get_coordinate_dictionary
class MoveGenerator:

    NOT_A_FILE = 0xFEFEFEFEFEFEFEFE
    NOT_B_FILE = 0xFDFDFDFDFDFDFDFD
    NOT_AB_FILE = 0xFCFCFCFCFCFCFCFC
    NOT_G_FILE = 0x7F7F7F7F7F7F7F7F
    NOT_H_FILE = 0xBFBFBFBFBFBFBFBF
    NOT_GH_FILE = 0x3F3F3F3F3F3F3F3F

    COORDINATES, INDICES = get_coordinate_dictionary()

    def __init__(self):
        pass

    @staticmethod
    def get_occupied_squares(bitboards):
        """Generates a bitboard of all occupied squares."""

        occupancies = dict()

        # Any pieces
        bitboard = 0
        for v in bitboards.values():
            bitboard |= v
        occupancies['any'] = bitboard

        # White pieces
        bitboard = 0
        for k in ['P', 'R', 'N', 'B', 'Q', 'K']:
            bitboard |= bitboards[k]
        occupancies['white'] = bitboard

        # Black pieces
        bitboard = 0
        for k in ['p', 'r', 'n', 'b', 'q', 'k']:
            bitboard |= bitboards[k]
        occupancies["black"] = bitboard

        # Empty
        occupancies['none'] = ~occupancies['any']
        
        return occupancies


    def get_lsf_bit_index(self, bitboard):
        """Gets index of least significant first bit."""

        if bitboard:
            return self.get_bitcount((bitboard & -bitboard) - 1)
        else:
            return -1
    
    @staticmethod
    def get_bitcount(bitboard):
        """Identifies the index of the first encountered bit."""
    
        count = 0
        while bitboard:
            count += 1
            bitboard &= bitboard - 1
        
        return count
            
    def get_moves(self, bitboards, game_state):
        """Generates a list of all legal moves in the current game state."""

        occupancies = self.get_occupied_squares(bitboards)
        occupied_squares = dict()
        for c in ['white', 'black', 'any', 'none']:
            squares = []
            for i in range(64):
                mask = 1 << i
                squares.append(1 if (occupancies[c] & mask) else 0)
            occupied_squares[c] = squares
        
    
        valid_moves = []

        # Get pawn moves
        pawn_moves = self.get_pawn_moves(bitboards, game_state, occupied_squares)
        if pawn_moves:
            valid_moves.extend(pawn_moves)

        return valid_moves

    def get_pawn_moves(self, bitboards, game_state, occupied_squares):
        """Generates a list of legal pawn moves."""

        # Represent en passant squares as occupied by opponent
        if game_state.get('en_passant', ''):
            en_passant = self.INDICES[game_state['en_passant']]
            opponent = 'white' if not game_state['white_turn'] else 'black'
            occupied_squares[opponent][en_passant] = 1

        white_turn = game_state['white_turn']
        piece = 'P' if white_turn else 'p'
        # Set up bitboard copy for get_lsf_bit_index() method
        tmp_board = bitboards[piece]
        pawn_moves = []

        # Loop through bitboard, get index for each pawn, and append possible moves to list
        while tmp_board:
            origin = self.get_lsf_bit_index(tmp_board)

            if white_turn:
                # Pawn pushes
                if not occupied_squares['any'][origin + 8]:
                    pawn_moves.append((origin, origin + 8))

                    # Allow for double move if pawn still on starting square
                    if 8 <= origin <= 15 and not occupied_squares['any'][origin + 16]:
                        pawn_moves.append((origin, origin + 16))
                
                # Pawn attacks
                ## If not a file and up_left is occupied by black, add attack
                if origin % 8 and occupied_squares['black'][origin + 7]:
                    pawn_moves.append((origin, origin + 7))

                ## If not h file and up_right is occupied by black, add attack
                if origin % 8 - 7 and occupied_squares['black'][origin + 9]:
                    pawn_moves.append((origin, origin + 9))

            else:
                # Pawn pushes
                if not occupied_squares['any'][origin - 8]:
                    pawn_moves.append((origin, origin - 8))
                
                # Allow for double move if pawn still on starting square
                    if 48 <= origin <= 55 and not occupied_squares['any'][origin - 18]:
                        pawn_moves.append((origin, origin - 16))

                # Pawn attacks
                ## If not a file and down_left is occupied by white, add attack
                if origin % 8 and occupied_squares['white'][origin - 9]:
                    pawn_moves.append((origin, origin - 9))

                ## If not h file and down_right is occupied by white, add attack
                if origin % 8 - 7 and occupied_squares['white'][origin - 7]:
                    pawn_moves.append((origin, origin - 7))

            # Remove index from tmp board
            tmp_board = (tmp_board & ~(1 << origin))
       
        return pawn_moves


    def get_knight_moves(self, bitboards, game_state, occupied_squares):
        """Generates a list of legal knight moves."""

        piece = 'N' if game_state['white_turn'] else 'n'
        opponent = 'white' if not game_state['white_turn'] else 'black'
        # Set up bitboard copy for get_lsf_bit_index() method
        tmp_board = bitboards[piece]
        knight_offsets = [-17, -15, -10, -6, 6, 10, 15, 17]
        knight_moves = []

        while tmp_board:
            origin = self.get_lsf_bit_index(tmp_board)
            tmp_board &= ~(1 << origin)

            for offset in knight_offsets:
                destination = origin + offset





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

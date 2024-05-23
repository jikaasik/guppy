import pytest
from guppy.board import Bitboard


@pytest.fixture
def board():
    return Bitboard()


@pytest.mark.parametrize('coordinates, index', [('a2', 8), ('b5', 33), ('g7', 54), ('h2', 15)])
def test_bitboard_indices(board, coordinates, index):
    assert board.INDICES[coordinates] == index


@pytest.mark.parametrize('index, coordinates', [(44, 'e6'), (13, 'f2'), (19, 'd3')])
def test_coordinates(board, index, coordinates):
    assert board.COORDINATES[index] == coordinates


def test_identify_occupant(board):
    assert board.identify_occupant(57) == 'n'
    assert board.identify_occupant(14) == 'P'
    assert board.identify_occupant(31) == None


@pytest.mark.parametrize(
    'fen, white_turn, castling_rights, en_passant, half_moves, move_count',
    [
        ('r1bq3r/ppp2kpp/1bn2n2/3p2B1/1PBp4/2P2N2/P4PPP/RN1QR1K1 w - - 2 12', True, set(), '', 2, 12),
        ('r7/ppp4k/5Rr1/1P5Q/8/8/P5PP/6K1 b - - 0 31', False, set(), '', 0, 31),
        ('8/7k/7P/7K/8/8/8/8 b - - 12 56', False, set(), '', 12, 56)
    ]
)
def test_parse_fen(board,
                   fen,
                   white_turn,
                   castling_rights,
                   en_passant,
                   half_moves,
                   move_count):
    board.parse_fen(fen)
    game_state = board.game_state

    assert game_state['white_turn'] == white_turn
    assert game_state['castling_rights'] == castling_rights
    assert game_state['en_passant'] == en_passant
    assert game_state['half_moves'] == half_moves
    assert game_state['move_count'] == move_count

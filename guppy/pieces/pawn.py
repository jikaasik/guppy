class Pawn:
    def move(pawns, origin, destination):
        pawns &= ~(1 << origin)
        pawns |= (1 << destination)
        return pawns
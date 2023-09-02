MARKERS = ["X", "O"]  # list of markers


class Player:
    """ This player class will create the player objects for the game.
        Initializes the object either as player 1 or 2 {self.player}
        And it will continuously ask the user to choose a marker from -
        The MARKERS list. It will not accept any other letter than these two"""

    def __init__(self, player):
        self.player = player
        self.marker = input(f"Player {self.player}, choose a marker either 'x' or 'o': ").upper()
        while self.marker not in MARKERS:
            self.marker = input(f"Player {self.player}, choose a marker either 'x' or 'o': ").upper()

    def position(self):
        """Prompt the player to choose a position on the board (1-9) and return it.
           The chosen position does not directly translate to an index on the board,
           as the board is a tuple of three separate lists. Subtraction of 1 is
           necessary to convert the chosen position to the correct index.
           See check_position method in TicTacToeBoard.py for implementation.
           :return int:
           """
        position = ''
        while True:
            try:
                position = int(input(f"Player {self.player}, please choose a position (1-9): "))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue

        return position

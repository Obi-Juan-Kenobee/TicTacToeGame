MARKERS = ["X", "O"]


class Player:

    def __init__(self, player):
        self.player = player
        self.marker = input(f"Player {self.player}, choose a marker either 'x' or 'o': ").upper()
        while self.marker not in MARKERS:
            self.marker = input(f"Player {self.player}, choose a marker either 'x' or 'o': ").upper()

    def position(self):
        position = ''
        while True:
            try:
                position = int(input(f"Player {self.player}, please choose a position (1-9): "))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue

        return position

class TicTacBoard:
    """
       Main class for the Tic Tac Toe Board.
       *Important* - The board is initialized as a tuple
       containing three separate lists.
       Contains the following methods:
       board - Prints the board.
       update_board - Prints the board.
       check_position - Checks the position selected is not taken.
       check_win - Checks if a winning condition has been met.
       check_tie - Checks for a tie.
       Please refer to individual methods for more info.
       """

    def __init__(self):
        self.row1 = ["", "", ""]
        self.row2 = ["", "", ""]
        self.row3 = ["", "", ""]

    def board(self):
        """
        This function prints the board to the console.
        It is mainly used to set up initial board -
        and to be passed into the functions that require a board -
        as a variable.
        :return tuple:
        """
        print(self.row1)
        print(self.row2)
        print(self.row3)

        return self.row1, self.row2, self.row3

    def update_board(self, board: tuple) -> tuple:
        """
        Args:
        board (tuple): The current state of the board.

        Returns:
        tuple: The updated board.
        :rtype: tuple
        """
        row1, row2, row3 = board
        print(row1)
        print(row2)
        print(row3)

        return row1, row2, row3

    def check_position(self, board: tuple, marker: str, position: int) -> tuple:
        """
         Check if the position picked by the player is available.
         If the position is already taken, prompt the user to choose another position.
         Returns False if the position is not taken to break out of the prompt loop.

        :param board: The game board.
        :param marker: The marker ('x' or 'o') to be placed on the board.
        :param position: The position chosen by the player.
        :return: The updated game board.
        :rtype: tuple
        """
        row1, row2, row3 = board
        while True:
            if 1 <= position <= 3:  # row1 on the board
                if row1[position - 1] != "":
                    print("That position is already taken, choose another.")
                    try:
                        position = int(input("Enter a position on the board: "))
                    except ValueError:
                        print("Please enter a valid number")

                else:
                    row1[position - 1] = marker
                    break

            elif 4 <= position <= 6:  # row2 on the board
                if row2[position - 4] != "":
                    print("That position is already taken, choose another.")
                    try:
                        position = int(input("Enter a position on the board: "))
                    except ValueError:
                        print("Please enter a valid number")

                else:
                    row2[position - 4] = marker
                    break

            elif 7 <= position <= 9:  # row3 on the board
                if row3[position - 7] != "":
                    print("That position is already taken, choose another.")
                    try:
                        position = int(input("Enter a position on the board: "))
                    except ValueError:
                        print("Please enter a valid number")

                else:
                    row3[position - 7] = marker
                    break

        return board

    def check_win(self, board: tuple, marker: str) -> bool:
        """
        Check if the player has won the game.
        Returns True if the player has won.
        :param board: tuple(list):
        :param marker: str:
        :return: bool:
        """
        row1, row2, row3 = board
        return ((row1[0] == marker and row2[0] == marker and row3[0] == marker)  # check row 1
                or (row1[1] == marker and row2[1] == marker and row3[1] == marker)  # check row 2
                or (row1[2] == marker and row2[2] == marker and row3[2] == marker)  # check row 3
                # check columns
                or (row1[0] == marker and row1[1] == marker and row1[2] == marker)
                or (row2[0] == marker and row2[1] == marker and row2[2] == marker)
                or (row3[0] == marker and row3[1] == marker and row3[2] == marker)
                # check diagonals
                or (row1[0] == marker and row2[1] == marker and row3[2] == marker)
                or (row1[2] == marker and row2[1] == marker and row3[0] == marker))

    def check_tie(self, board: tuple) -> bool:
        """
        Check if the game is a tie.
        Returns True if the game is a tie.
        :param board: tuple(list):
        :return: bool:
        """
        row1, row2, row3 = board  # unpacking of rows to avoid using messy nested loops
        if "" in row1 or "" in row2 or "" in row3:
            return False
        else:
            print("It's a tie!")
            return True

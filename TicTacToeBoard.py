class TicTacBoard:

    def __init__(self):
        self.row1 = ["", "", ""]
        self.row2 = ["", "", ""]
        self.row3 = ["", "", ""]

    def board(self):
        print(self.row1)
        print(self.row2)
        print(self.row3)

        return self.row1, self.row2, self.row3

    def update_board(self, board):
        row1, row2, row3 = board
        print(row1)
        print(row2)
        print(row3)

        return row1, row2, row3

    def check_position(self, board, marker, position):
        row1, row2, row3 = board
        while True:
            if 1 <= position <= 3:
                if row1[position - 1] != "":
                    print("That position is already taken, choose another.")
                    try:
                        position = int(input("Enter a position on the board: "))
                    except ValueError:
                        print("Please enter a valid number")

                else:
                    row1[position - 1] = marker
                    return False

            elif 4 <= position <= 6:
                if row2[position - 4] != "":
                    print("That position is already taken, choose another.")
                    try:
                        position = int(input("Enter a position on the board: "))
                    except ValueError:
                        print("Please enter a valid number")

                else:
                    row2[position - 4] = marker
                    return False

            elif 7 <= position <= 9:
                if row3[position - 7] != "":
                    print("That position is already taken, choose another.")
                    try:
                        position = int(input("Enter a position on the board: "))
                    except ValueError:
                        print("Please enter a valid number")

                else:
                    row3[position - 7] = marker
                    return False

        return board

    def check_win(self, board, marker):
        row1, row2, row3 = board
        return ((row1[0] == marker and row2[0] == marker and row3[0] == marker)
            or (row1[1] == marker and row2[1] == marker and row3[1] == marker)
            or (row1[2] == marker and row2[2] == marker and row3[2] == marker)
            or (row1[0] == marker and row1[1] == marker and row1[2] == marker)
            or (row2[0] == marker and row2[1] == marker and row2[2] == marker)
            or (row3[0] == marker and row3[1] == marker and row3[2] == marker)
            or (row1[0] == marker and row2[1] == marker and row3[2] == marker)
            or (row1[2] == marker and row2[1] == marker and row3[0] == marker))

    def check_tie(self, board):
        row1, row2, row3 = board # unpacking of rows to avoid using multiple for loops
        if "" in row1 or "" in row2 or "" in row3:
            return False
        else:
            print("It's a tie!")
            return True

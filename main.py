from TicTacToeBoard import *
from Players import *

tic_tac_board = TicTacBoard()
print("# Tic Tac Toe Game #")

player1 = Player(1)
player2 = Player(2)

playing = True  # variable to control the game
while playing:  # main game loop
    print("# Playing ... #")
    board = tic_tac_board.board()
    # Player 1 turn
    p1_pos = player1.position()
    tic_tac_board.check_position(board, player1.marker, p1_pos)
    tic_tac_board.update_board(board)
    if tic_tac_board.check_win(board, player1.marker):
        print(f"Player {player1.marker} Wins!")
        playing = False

    elif tic_tac_board.check_tie(board):
        playing = False

    else:
        # Player 2 turn
        p2_pos = player2.position()
        check_pos_choice_p2 = tic_tac_board.check_position(board, player2.marker, p2_pos)
        tic_tac_board.update_board(board)
        if tic_tac_board.check_win(board, player2.marker):
            print(f"Player {player2.marker} Wins!")
            playing = False

        elif tic_tac_board.check_tie(board):
            playing = False


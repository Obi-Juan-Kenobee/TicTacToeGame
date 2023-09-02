from TicTacToeBoard import *
from Players import *

tic_tac_board = TicTacBoard()
print("# Tic Tac Toe Game #")

player1 = Player(1)
player2 = Player(2)

playing = True
while playing:
    print("# Playing ... #")
    board = tic_tac_board.board()

    p1_pos = player1.position()
    check_pos_choice_p1 = tic_tac_board.check_position(board, player1.marker, p1_pos)
    tic_tac_board.update_board(board)
    if tic_tac_board.check_win(board, player1.marker):
        print(f"Player {player1.marker} Wins!")
        playing = False

    elif tic_tac_board.check_tie(board):
        playing = False

    else:
        p2_pos = player2.position()
        check_pos_choice_p2 = tic_tac_board.check_position(board, player2.marker, p2_pos)
        tic_tac_board.update_board(board)
        if tic_tac_board.check_win(board, player2.marker):
            print(f"Player {player2.marker} Wins!")
            playing = False

        elif tic_tac_board.check_tie(board):
            playing = False

    # if not check_pos_choice_p1 or not check_pos_choice_p2:
    #     continue
    # else:
    #
    #     check_win_p2 =
    #     if check_win_p1 or check_win_p2:
    #         playing = False
    #
    #     elif not tic_tac_board.check_tie(board):
    #         playing = False
    #     else:
    #         continue
from TicTacToeLibrary import Board
from TicTacToeLibrary import Action

# https://napuzba.com/a/import-error-relative-no-parent/p2 for trouble with importing

board = Board()
user_symbol = board.x_or_o()
action = Action(user_symbol)


def game():
    while True:
        action.user_turn(board.values)

        action.win_detection(board.values)
        action.draw_condition(board.values)
        if action.game_ended:
            play_again = action.play_again_prompt()
            if play_again:
                board.values = [" " for field in range(1, 10, 1)]
                break
            else:
                return

        action.bot_turn(board.values)
        action.win_detection(board.values)
        action.draw_condition(board.values)
        if action.game_ended:
            play_again = action.play_again_prompt()
            if play_again:
                board.values = [" " for field in range(1, 10, 1)]
                break
            else:
                return
    return game()


# To-do: find a way for the player to change symbols after a game? Win count?


game()

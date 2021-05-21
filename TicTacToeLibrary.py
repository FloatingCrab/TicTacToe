import random

# here are the classes for the playing board and all the actions while playing
class Board:
    def __init__(self):
        self.values = [" " for field in range(1, 10, 1)]
        self.fields = " {0} | {1} | {2}\n ---------\n {3} | {4} | {5}\n ---------\n {6} | {7} | {8}".format(
            self.values[0],
            self.values[1],
            self.values[2],
            self.values[3],
            self.values[4],
            self.values[5],
            self.values[6],
            self.values[7],
            self.values[8])

    def x_or_o(self):
        symbol = "x"
        while True:
            res = input("Do you want to be X or O?\n")
            if res == "X":
                print("You chose x!")
                symbol = "x"
                return symbol
            elif res == "x":
                print("You chose x!")
                symbol = "x"
                return symbol
            elif res == "o":
                print("You chose o!")
                symbol = "o"
                return symbol
            elif res == "O":
                print("You chose o!")
                symbol = "o"
                return symbol
            else:
                print("You can press x or o on your keyboard.")


# Action includes player and bot turns and maybe win condition detection, not sure yet.

class Action:
    def __init__(self, symbol):
        self.symbol = symbol
        self.current_field = None
        self.turn_counter = random.randint(0, 1)
        if self.symbol == "x":
            self.bot_symbol = "o"
        elif self.symbol == "o":
            self.bot_symbol = "x"
        self.first_turn = True
        self.current_symbol = None
        self.game_ended = False

    # user_turn lets the user pick a number between 1 and 9 and then adds the user symbol to the board values.
    # then it prints out the current field, which consists of the board values.
    def user_turn(self, board_values):
        print("Where do you wanna set your point? 1 is top left, 9 is bottom right etc.\n")
        while True:
            res = input()

            if res in [str(num) for num in range(1, 10, 1)]:
                for i in range(0, 10, 1):
                    if int(res) - 1 == i:
                        if board_values[i] == " ":
                            board_values[i] = self.symbol
                            # current_field doesn't update automatically with each board_value change >:(
                            self.current_field = " {0} | {1} | {2}\n ---------\n {3} | {4} | {5}\n ---------\n {6} | {7} | {8}".format(
                                board_values[0],
                                board_values[1],
                                board_values[2],
                                board_values[3],
                                board_values[4],
                                board_values[5],
                                board_values[6],
                                board_values[7],
                                board_values[8])
                            print("Your turn:")
                            print(self.current_field + "\n")
                            self.turn_counter += 1
                            self.current_symbol = self.symbol
                            # print(self.current_symbol)
                            # print(board_value)
                            return board_values

            else:
                print("Please choose a number between 1 and 10 D: \n")
            print("That field is already taken :(")

    def bot_turn(self, board_values):
        print("The bot's turn:")
        # if self.first_turn = True:
        # in the future maybe a smart bot, one that only picks the fields near their moves on the board?
        while True:
            bot_move = random.randint(0, 8)
            self.current_symbol = self.bot_symbol
            if board_values[bot_move] == " ":
                board_values[bot_move] = self.bot_symbol
                self.current_field = " {0} | {1} | {2}\n ---------\n {3} | {4} | {5}\n ---------\n {6} | {7} | {8}".format(
                    board_values[0],
                    board_values[1],
                    board_values[2],
                    board_values[3],
                    board_values[4],
                    board_values[5],
                    board_values[6],
                    board_values[7],
                    board_values[8])
                self.first_turn = False
                print(self.current_field)
                self.current_symbol = self.bot_symbol
                # print(self.current_symbol)
                # print(board_value)
                return board_values
            else:
                pass

    def win_detection(self, board_values):
        if self.game_ended == False:
            while True:
                if board_values[0] == self.current_symbol and board_values[1] == self.current_symbol and board_values[
                    2] == self.current_symbol:
                    self.game_ended = True
                    if self.current_symbol == self.bot_symbol:
                        return print("Oh no! You lost!")
                    elif self.current_symbol == self.symbol:
                        return print("WOOOOO! YOU WON! :D")
                elif board_values[3] == self.current_symbol and board_values[4] == self.current_symbol and board_values[
                    5] == self.current_symbol:
                    self.game_ended = True
                    if self.current_symbol == self.bot_symbol:
                        return print("Oh no! You lost!")
                    elif self.current_symbol == self.symbol:
                        return print("WOOOOO! YOU WON! :D")
                elif board_values[6] == self.current_symbol and board_values[7] == self.current_symbol and board_values[
                    8] == self.current_symbol:
                    self.game_ended = True
                    if self.current_symbol == self.bot_symbol:
                        return print("Oh no! You lost!")
                    elif self.current_symbol == self.symbol:
                        return print("WOOOOO! YOU WON! :D")
                elif board_values[0] == self.current_symbol and board_values[3] == self.current_symbol and board_values[
                    6] == self.current_symbol:
                    self.game_ended = True
                    if self.current_symbol == self.bot_symbol:
                        return print("Oh no! You lost!")
                    elif self.current_symbol == self.symbol:
                        return print("WOOOOO! YOU WON! :D")
                elif board_values[1] == self.current_symbol and board_values[4] == self.current_symbol and board_values[
                    7] == self.current_symbol:
                    self.game_ended = True
                    if self.current_symbol == self.bot_symbol:
                        return print("Oh no! You lost!")
                    elif self.current_symbol == self.symbol:
                        return print("WOOOOO! YOU WON! :D")
                elif board_values[3] == self.current_symbol and board_values[5] == self.current_symbol and board_values[
                    8] == self.current_symbol:
                    self.game_ended = True
                    if self.current_symbol == self.bot_symbol:
                        return print("Oh no! You lost!")
                    elif self.current_symbol == self.symbol:
                        return print("WOOOOO! YOU WON! :D")
                elif board_values[0] == self.current_symbol and board_values[4] == self.current_symbol and board_values[
                    8] == self.current_symbol:
                    self.game_ended = True
                    if self.current_symbol == self.bot_symbol:
                        return print("Oh no! You lost!")
                    elif self.current_symbol == self.symbol:
                        return print("WOOOOO! YOU WON! :D")
                elif board_values[6] == self.current_symbol and board_values[4] == self.current_symbol and board_values[
                    2] == self.current_symbol:
                    self.game_ended = True
                    if self.current_symbol == self.bot_symbol:
                        return print("Oh no! You lost!")
                    elif self.current_symbol == self.symbol:
                        return print("WOOOOO! YOU WON! :D")
                else:
                    return
        else:
            pass

    def draw_condition(self, board_values):
        if not self.game_ended:

            count = 0
            for i in board_values:
                if i != " ":
                    count += 1
            if count == 9:
                self.game_ended = True
                print("It's a DRAW!")
        else:
            pass

    def play_again_prompt(self):
        print("Do you want to play another round? \n [y] [n]\n")
        while True:
            answer = input()
            if answer == "y":
                return True
            elif answer == "n":
                return False
            else:
                print("Please give a valid answer :( You can just close the window as well.\n [y] [n]\n")
# board = Board()
# action = Action("x")
# action.user_turn()
# action.bot_turn()

import random
import sys

moves = ["rock",  "paper",  "scissor"]
cycle_counter = -1


class Player:
    no_of_rounds = 0
    score = 0
    round_move = ""
    self_move = ""
    opponent_move = ""


class Computer_player_random(Player):
    def move(self):
        self.round_move = random.choice(moves)
        self.no_of_rounds += 1
        return self.round_move

    def remembering(self,  human_move,  cp_move):
        self.self_move = cp_move
        self.opponent_move = human_move


class Computer_player_cycle(Player):

    def move(self):
        global cycle_counter
        cycle_counter += 1
        if(cycle_counter > 2):
            cycle_counter = 0
        self.round_move = moves[cycle_counter]

        if(cycle_counter > 2):
            cycle_counter = 0
        self.no_of_rounds += 1
        return self.round_move

    def remembering(self, human_move, cp_move):
        self.self_move = cp_move
        self.opponent_move = human_move


class Computer_player_imitator(Player):
    def move(self):

        if self.no_of_rounds == 0 or self.opponent_move == "":
            self.round_move = "scissor"
        else:
            self.round_move = self.opponent_move
        self.no_of_rounds += 1
        return self.round_move

    def remembering(self, h_move, cp_move):
        self.self_move = cp_move
        if h_move == "rock" or h_move == "paper" or h_move == "scissor":
            self.opponent_move = h_move
        else:
            pass


class Computer_player_fixed_move(Player):
    def move(self):
        self.round_move = "rock"
        return self.round_move

    def remembering(self, human_move, cp_move):
        self.self_move = cp_move
        self.opponent_move = human_move


class Human_player(Player):
    def move(self):
        self.round_move = input("\nEnter your move : ")
        self.round_move = self.round_move.lower()
        return self.round_move

    def remembering(self):
        pass


class Game():

    def __init__(self, human_player, opponent_cp):
        self.human_player = human_player
        self.opponent_cp = opponent_cp
        self.match_type()

    def match_type(self):
        print("Play a single round?")
        self.type_of_round = input("\nPlay a match?\n(Round/Match)\n")
        self.type_of_round = self.type_of_round.lower()

        if self.type_of_round == "match":
            i = self.round_type()
            self.multiple_round(i, self.human_player, self.opponent_cp)
        elif self.type_of_round == "round":
            self.single_round(self.human_player, self.opponent_cp)
        else:
            print("Wrong input")
            start = Game(human_player, opponent_cp)

    def round_type(self):
        try:
            diffi = int(input("Enter number of rounds in the match. (3/5/7)"))
        except ValueError:
            print("Wrong choice")
            return self.round_type()
        else:
            if(diffi == 3 or diffi == 5 or diffi == 7):
                return diffi
            else:
                print("Wrong choice")
                return self.round_type()

    def multiple_round(self, i, human_player, opponent_cp):
        while(i):
            human_move = human_player.move()
            cp_move = opponent_cp.move()
            flag = result(human_move, cp_move, self.type_of_round)
            if flag == 0:
                print("\nENTER AGAIN : \n")
                self.multiple_round(i, human_player, opponent_cp)
            i -= 1
            human_player.remembering()
            opponent_cp.remembering(human_move, cp_move)
        self.print_final_output()

    def single_round(self, human_player, opponent_cp):
        human_move = human_player.move()
        cp_move = opponent_cp.move()
        flag = result(human_move, cp_move, self.type_of_round)
        if flag == 0:
            print("\nENTER AGAIN : \n")
            self.single_round(human_player, opponent_cp)
        human_player.remembering()
        opponent_cp.remembering(human_move, cp_move)
        self.print_final_output()

    def print_final_output(self):
        print("\nFinal Score:\n\nYour score: ", self.human_player.score)
        print("Computer score: ", self.opponent_cp.score)
        if(self.human_player.score > self.opponent_cp.score):
            print("\nCongrats. You win")
        elif(self.human_player.score < self.opponent_cp.score):
            print("Hard luck. You lose")
        else:
            print("OOPS!! It's a tie")
        print("*" * 150)
        sys.exit()


def result(mov1, mov2, choice):
    print("\nComputer chose : ", mov2)
    if mov1 == mov2:
        print("That's a tie")
    elif mov1 == "rock" and mov2 == "scissor":
        print("You win. ", mov1, "beats", mov2)
        human_player.score += 1
    elif mov1 == "paper" and mov2 == "rock":
        print("You win. ", mov1, "beats", mov2)
        human_player.score += 1
    elif mov1 == "scissor" and mov2 == "paper":
        print("You win. ", mov1, "beats", mov2)
        human_player.score += 1
    elif mov1 == "paper" and mov2 == "scissor":
        print("You lose.", mov2, "beats", mov1)
        opponent_cp.score += 1
    elif mov1 == "scissor" and mov2 == "rock":
        print("You lose.", mov2, "beats", mov1)
        opponent_cp.score += 1
    elif mov1 == "rock" and mov2 == "paper":
        print("You lose.", mov2, "beats", mov1)
        opponent_cp.score += 1
    else:
        print("Wrong Input")

        return 0

    human_player.no_of_rounds += 1
    opponent_cp.no_of_rounds += 1
    if choice == "match":
        print("\n\n")  # blank print statement for next line to conform to pep8
        print("*" * 150)
        print("Round ", human_player.no_of_rounds, " result:")
        print("Your score: ", human_player.score)
        print("\nComputer score: ", opponent_cp.score)
        print("*" * 150)
    else:
        print("*" * 150)
        print("Final Score:\n\nYour score: ", human_player.score)
        print("Computer score: ", opponent_cp.score)
        if(human_player.score > opponent_cp.score):
            print("\nCongrats. You win")
        elif(human_player.score < opponent_cp.score):
            print("Hard luck. You lose")
        else:
            print("OOPS!! It's a tie")
        print("*" * 150)
        sys.exit()
    return 1


cp1 = Computer_player_random()
cp2 = Computer_player_cycle()
cp3 = Computer_player_imitator()
cp4 = Computer_player_fixed_move()

cp_list = [cp1, cp2, cp3, cp4]
opponent_cp = random.choice(cp_list)
human_player = Human_player()

print("\n--------------Let's play Rock, Paper, Scissor--------------\n")

start = Game(human_player, opponent_cp)

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = None

    def make_choice(self):
        while True:
            choice = input("Choose one from Rock, Paper, or Scissor:").lower()
            if choice in ["rock", "paper", "scissor"]:
                self.choice = choice
                break
            print("Invalid Choice: Choose one from Rock, Paper, or Scissor")

class Computer(Player):
    def __init__(self):
        super().__init__("Computer")

    def make_choice(self):
        self.choice = random.choice(["rock", "paper", "scissor"])

class Game:
    def __init__(self):
        player_name = input("Input player's name:")
        self.player = Player(name = player_name)
        self.computer = Computer()
        self.tie = 0

    def check_winner(self):
        winner = {
                    "rock": "scissor",
                    "scissor": "paper",
                    "paper": "rock"
                  }
        print(f'''{self.player.name} selected {self.player.choice} and Computer selected {self.computer.choice}''')
        if self.player.choice == self.computer.choice:
            print("It's a tie!")
            self.tie += 1

        elif self.computer.choice == winner [self.player.choice]:
            print(f'''{self.player.name} wins!''')
            self.player.score += 1

        else:
            print("Computer wins!")
            self.computer.score += 1

    def play(self) :
        while True:
            try:
                self.number_of_games = int(input("How many games would you like to play?"))
                if self.number_of_games > 0:
                    break
                print("Invalid input. Please enter a positive integer")
            except ValueError:
                print("Invalid input. Please enter an integer")

        self.game_number = 1
        while self.game_number <= self.number_of_games:
            print(f"Game number: {self.game_number} of {self.number_of_games}")
            self.player.make_choice()
            self.computer.make_choice()
            self.check_winner()
            self.game_number += 1

        print("*" * 30)
        print("Score:")
        print(f'''Total Games: {self.number_of_games}''')
        print(f'''{self.player.name} won: {self.player.score}''')
        print(f'''Computer won: {self.computer.score}''')
        print(f'''Tied: {self.tie}''')

g= Game()
g.play()
import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.score = 0

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        while True:
            response = input("Rock, Paper, Scissors?\n").lower()
            if response not in moves:
                print("Please type in Rock, Paper, Scissors")
            else:
                return response


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.new_move = moves[0]

    def move(self):
        return self.new_move

    def learn(self, my_move, their_move):
        self.new_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.new_move = moves[0]
        self.current_index = 0

    def move(self):
        return self.new_move

    def learn(self, my_move, their_move):
        self.current_index = moves.index(my_move)
        self.new_move = moves[(self.current_index + 1) % len(moves)]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def calculate_score(self, move1, move2):
        if beats(move1, move2):
            print("Player 1 wins this round!")
            return 1, 0
        elif beats(move2, move1):
            print("Player 2 wins this round!")
            return 0, 1
        else:
            print("Game Tied!")
            return 0, 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        round_score_p1, round_score_p2 = self.calculate_score(move1, move2)
        self.p1.score += round_score_p1
        self.p2.score += round_score_p2
        print("Round score:")
        print(f"Player 1: {round_score_p1}, Player 2: {round_score_p2}\n")

    def play_game(self):
        print("Game start!")
        while (True):
            rounds = int(input("How many rounds would you like to play?\n"))
            if rounds <= 0:
                print("Invalid number of rounds, Please enter a number again ")
            else:
                break

        for round in range(rounds):
            print(f"Round {round}:")
            self.play_round()

        print("Final scores:")
        print(f"Player 1: {self.p1.score}")
        print(f"Player 2: {self.p2.score}\n")

        if self.p1.score > self.p2.score:
            print("Player 1 Wins the game!")
        elif self.p1.score < self.p2.score:
            print("Player 2 Wins the game!")
        else:
            print("No Winner! It's a draw!")

        print("\nGame over!\n")


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def intro():
    print("Welcome to Rock Paper Scissors!")
    print("Type Starter, Easy, Medium, or Hard to Begin!\nType Exit to quit")


def validate_input():
    while (True):
        intro()
        while (True):
            print("Please select a game mode")
            response = input().lower()
            if response == "exit":
                print("Thanks for playing!\n")
                return
            elif response == "starter":
                print("Starter mode selected")
                game = Game(HumanPlayer(), AllRockPlayer())
                game.play_game()
                break
            elif response == "easy":
                print("Easy mode selected")
                game = Game(HumanPlayer(), ReflectPlayer())
                game.play_game()
                break
            elif response == "medium":
                print("Medium mode selected")
                game = Game(HumanPlayer(), CyclePlayer())
                game.play_game()
                break
            elif response == "hard":
                print("Hard mode selected")
                game = Game(HumanPlayer(), RandomPlayer())
                game.play_game()
                break
            else:
                print("Please type in starter, easy, medium, hard or exit.")


def start_Game():
    intro()
    validate_input()


if __name__ == '__main__':
    start_Game()

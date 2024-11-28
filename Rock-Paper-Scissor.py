# This is a simple game Rock, Paper and Scissor implemented in Python.
import random


class Rps:
    def game(self):
        play = True
        computer_score = 0
        player_score = 0
        choices = ("rock", "paper", "scissor")

        while play:
            print("Type QUIT to quit the game")
            try:
                player_choice = input("Rock, Paper or Scissor: ")
                if player_choice not in choices:
                    raise ValueError
            except ValueError as err:
                print(err)
                print("Please enter a valid choice!")
            except Exception as err:
                print(err)
            computer_choice = random.choice(choices)
            print("Computer's choice is: ", computer_choice)
            if player_choice.lower() == "rock":
                if computer_choice == "paper":
                    computer_score += 1
                    self.computer_gets_a_score()
                elif computer_choice == "scissor":
                    player_score += 1
                    self.player_gets_a_score()
            elif player_choice.lower() == "paper":
                if computer_choice == "rock":
                    player_score += 1
                    self.player_gets_a_score()
                elif computer_choice == "scissor":
                    computer_score += 1
                    self.computer_gets_a_score()
            elif player_choice.lower() == "scissor":
                if computer_choice == "rock":
                    computer_score += 1
                    self.computer_gets_a_score()
                elif computer_choice == "paper":
                    player_score += 1
                    self.player_gets_a_score()
            elif player_choice.upper() == "QUIT":
                play = False
                self.declare_winner(player_score, computer_score)

            else:
                print("Player's choice is invalid!")

    def computer_gets_a_score(self):
        print("Yaay!! Computer gets a score!")

    def player_gets_a_score(self):
        print("Yiippiieee!! Player gets a score!")

    def declare_winner(self, player_score, computer_score):
        print("Player Score: ", player_score)
        print("Computer Score: ", computer_score)
        if player_score == computer_score:
            print("Both are WINNERS!")
        else:
            print("And the Winner is: ", ("PLAYER" if player_score > computer_score else "COMPUTER"),
                  "!!! Congratulations! :)")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rps = Rps()
    rps.game()

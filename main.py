import random as rand

class MAIN:
    def __init__(self):
        self.game = GAME()
        pass

    def main(self):
        self.game.main()

        self.again()
        pass
    def again(self):
        if input("Play again? (y/n): ").lower() == "y":
            self.main()
        else:
            print("Goodbye!")

class GAME:
    def __init__(self):
        pass

    def main(self):
        final = self.winner()
        if final == "tie":
            print("Tie!")
        elif final == "user":
            print("You win!")
        else:
            print("Computer wins!")

        
        pass
    def get_input(self):
        user = input("rock paper scissors \nEnter your choice: ")
        userL = user.lower()
        choices = ['rock', 'paper', 'scissors']
        try:
            result = choices.index(userL)
        except ValueError:
            print("Invalid input")
            return self.get_input()
        return result
    def get_random(self):
        return rand.randint(0,2)
    def winner(self):
        computer = self.get_random()
        user = self.get_input()
        if user == 0:
            if computer == 0:
                return "tie"
            elif computer == 1:
                return "user"
            else:
                return "computer"
            pass
        elif user == 1:
            if computer == 0:
                return "computer"
            elif computer == 1:
                return "tie"
            else:
                return "user"
            pass
        elif user == 2:
            if computer == 0:
                return "user"
            elif computer == 1:
                return "computer"
            else:
                return "tie"

            pass
main = MAIN()
main.main()
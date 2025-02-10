# Rock-Paper-Scissors game
from random import choice

inputs = ["rock", "paper", "scissors"]

# computerChoice = choice(inputs)
while True:
    userInput = input("Enter either Rock, Paper or Scissors or 'q' to quit: ").lower()
    if userInput == "q":
        break
    if userInput not in inputs:
        print("Error input..")
        continue
    computerChoice = choice(inputs)
    print(f"Computer choice: {computerChoice}")


    if userInput == "rock" and computerChoice == "scissors":
        print("Rock crushes Scissors, and you win!")

    elif userInput == "scissors" and computerChoice == "paper":
        print("Scissors cuts Paper, and you win!")

    elif userInput == "paper" and computerChoice == "rock":
        print("Paper covers Rock, and you win!")

    elif userInput == computerChoice:
        print("It's a tie, try again.")

    else:
        print("Sorry, you failed. Try again.")

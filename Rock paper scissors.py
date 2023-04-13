import random
import os

choises = ("Rock","Paper","Scissors")
computer = random.choice(choises)

while True:
    player = None

    while player not in choises:
        player = input("Rock, paper or scissors?  ").capitalize()

    print("Computer = " + computer)
    print("Player = " + player)

    if player == computer:
        print("Tie")

    if player == "Rock":
        if computer == "Scissors":
            print("You won!!")
        else:
            print("You lose")

    if player == "Scissors":
        if computer == "Paper":
            print("You won!!")
        else:
            print("You lose")

    if player == "Paper":
        if computer == "Rock":
            print("You won!!")
        else:
            print("You lose")

    again = input("Do you want to play again? ")

    if again == "yes":
        os.system("clear")
    else:
        break

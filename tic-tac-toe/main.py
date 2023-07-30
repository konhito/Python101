import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock , paper or scissors?: ").lower()

    if player == computer:
        print(f"Computer: {computer}")
        print(f"player: {player}")
        print("IT's a tie ")

    elif player == "rock":
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"player: {player}")
            print("You loose! ")
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"player: {player}")
            print("You win! ")
    elif player == "paper":
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"player: {player}")
            print("You loose! ")
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"player: {player}")
            print("You win! ")
    elif player == "scissors":
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"player: {player}")
            print("You loose! ")
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"player: {player}")
            print("You win! ")

    play_again = input("plaay again? (yes/no): ").lower()

    if play_again != "yes":
        break
print("BYE! amogos")

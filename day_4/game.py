import random

# Write a program to simulate a game rock, paper, scissors between user and the computer.

# variables
options = ["paper", "rock", "scissors"]
comp = random.choice(options)

while True:
    user = input("Choose an option between rock, paper, scissors: ").lower()
    if user in options:
        break
    else:
        print("Invalid option. Please choose between rock, paper, or scissors.")

if user == comp:
    print("Draw!")
elif (user == 'paper' and comp == 'rock') or (user == 'rock' and comp == 'scissors') or (user == 'scissors' and comp == 'paper'):
    print("The winner is the user!")
else:
    print("The winner is the computer!")

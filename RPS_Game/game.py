# ROCK - PAPER _ SCISSOR MiniGame for CodeYou

import random

# Define our choices
choices = ["rock", "paper", "scissors"]

# Control variable for the while loop
is_valid = False

# Print valid values tips
print(f"\nValues allowed: ROCK - PAPER - SCISSORS\n")

# Loop to control user choice is a valid one, in case of a wrong value try again
while is_valid == False:
    user_pick = str.lower(input("Choose your pick: "))
    if user_pick not in choices:
        print("\nUser pick isn't a valid choice, please try again\n")
    else:
        is_valid = True

# Select random value for computer choice
ai_pick = random.choice(choices)

# Print values from both
print(f"\nUser choose: {str.upper(user_pick)} \nAI choose: {str.upper(ai_pick)}\n")

# Check choices and declare a winner or a tie
if user_pick == ai_pick:
    print("It's a TIE, no winner \U0001F62C")
    exit()
if user_pick == "rock" and ai_pick == "scissors":
    print("User WON \U0001F60E")
elif user_pick == "paper" and ai_pick == "rock":
    print("User WON \U0001F60E")
elif user_pick == "scissors" and ai_pick == "paper":
    print("User WON \U0001F60E")
else:
    print("AI WON \U0001F62D")
# randomly pick a number between 1 and 6.
# If 1 user picked dice with 1
# if 2 user picked dice with 2
# and so on.

import random

def main():


    print("This is the dice game.") 
    guess = int(input("Please guess what the value of the six sided die will be" + 
    " after it has been \"rolled\" (choose an integer 1 through 6): "))

    while guess < 1 or guess > 6:
        print("That input is invalid, please try again.")
        guess = int(input("Please guess what the value of the six sided die will be" + 
        " after it has been \"rolled\" (choose an integer 1 through 6): "))

    dice = random.randrange(1,7)
    # print(dice)

    if guess == dice:
        win_lose = "win"
    else:
        win_lose = "lose"
    
    print(f"You guessed the dice landed on {guess}. The dice landed on {dice}, so you {win_lose}!")



main()
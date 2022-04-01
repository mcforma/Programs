# File:    AhsForbes.py 
# Project: CSIS2101 Assignment 6
# Author:  Matthew Forbes 
# History: Version 1.1 February 11, 2022

'''
#1 The purpose of this program is to build our own version of Rock Paper and Scissors
using comic characters. 

1.	The user's choice of AQ, HU or SW at the keyboard should be passed in as the argument 
for the function. 
    a.	AQ - user picks Aqua man
    b.	HU - user picks Human Torch
    c.	SW - user picks Swamp Thing

2.	If the user enters a wrong choice other than AQ HU or SW ask the user to enter again 
using a while loop. 

3.	Then the program should pick a random number generated as 0, 5 or 10. If the number is 0, 
computer has chosen Aqua man, if the number is 5 computer has chosen Human Torch and if 10 
computer has chosen Swamp Thing.  Cannot use a choice function. 

4.	The computers choice is displayed. (This should not be displayed until the user has picked 
the choice.)

5.	A winner is selected according to the following rules. 
    a.	If one player chooses Aqua man and other player chooses Human Torch  then Aqua man wins. 
    (Aqua man extinguishes Human Torch.)
    b.	If one player chooses Human Torch and other player chooses Swamp Thing then Human Torch 
    wins. (Human Torch burns Swamp Thing)
    c.	If one player chooses Swamp Thing and other player chooses Aqua Man then Swamp Thing wins.
    (Swamp Thing drowns Aqua man)
    d.	If both players make the same choice it should say “Tie, please play again.” And the game 
    must be played again to determine the winner. When the game is replayed the user and computer 
    have to choose again. 

6.	The function should be named as AHSLastName (your lastname in place of lastname) and should have 
one argument passed into the function which is a two characters string. 

'''

# import random library in order to use randrange()
import random


# Introductory info and rules displayed to user
def main():

    # provide intro explanation to user of what program is and the rules
    print("Hello, this is rock paper scissors but with comic characters. Let me explain the rules.")
    print("The player will choose one of the three characters via a two character abbreviation (listed below).")
    print("This selection will be compared with a random character selection by the computer. The results\n" +
    "and who won will be displayed.")

    print("\nThe options are: \"AQ\" (Aqua man), \"HU\" (Human Torch), \"SW\" (Swamp Thing). All other inputs\n" + 
    "are invalid and the player will be asked to enter their choice repeatedly until a valid choice is entered.")
    print("\nAqua man beats Human Torch. Human Torch beats Swamp Thing. Swamp Thing beats Aqua Man. In the event\n" +
    "of a tie, the game will be played again and the player and computer must make another selection.")

    # Gets user input and assigns to user_selection variable
    user_selection = Get_User_Choice()

    # after valid entry has been input, pass user choice as argument to function for processing.
    # user's choice is passed as user_selection
    AHSForbes(user_selection)



# Input
# Get User Choice function definition . A function does one thing that is needed more than once
def Get_User_Choice():

    # get user choice indicating only valid options in prompt as a reminder
    user_choice = input("\nPlease select a character (\"AQ\", \"HU\", or \"SW\"): ")
    # return uppercase copy of user input in case they input lowercase letters
    user_upper = user_choice.upper()

    # while user input invalid, loop until valid
    while user_upper != "AQ" and user_upper != "HU" and user_upper != "SW":
        print("\nInvalid input. The only valid inputs are: \"AQ\", \"HU\", and \"SW\". Please try again.")
        user_choice = input("Please select a character (\"AQ\", \"HU\", or \"SW\"): ")
        user_upper = user_choice.upper()
    
    # return validated user selection to calling function and assign result to user_selection in main function
    # Since the while loop has provided input validation, the only argument provided to the function is a two
    # character string matching the above choices (AQ, HU, SW)
    return user_upper



# Processing and Output
# AHSForbes function definition
def AHSForbes(usr_sel):
    
    # Create win/lose constants to eliminate possiblity of typo, especially during ifs/elifs
    WON = "won"
    LOST = "lost"

    # use randrange(). First integer is starting number, second is upper limit, third is skip count (add 5 every iteration)
    rand_num = random.randrange(0,11,5)     # assign result to variable
    if rand_num == 0:   # if random number is 0, computer's selection is AQ
        comp_sel = "AQ"
    elif rand_num == 5:     # if 5, computer's selection is HU
        comp_sel = "HU"
    elif rand_num == 10:    # if 10, computer's selecthuion is SW
        comp_sel = "SW"

    # Check for tie. If tie inform player it is a tie and get their input and call again.
    while usr_sel == comp_sel:
        print(f"The computer also (randomly) selected {comp_sel}.")
        print("Tie, please play again.")
        usr_sel = Get_User_Choice()

    # Account for all different combinations of character selection by checking the three options the user could pick, 
    # and the subsequent options the computer could pick (given that ties were already handled). 
    # Then identify character who won for print statements below.
    if usr_sel == "AQ":
        if comp_sel == "HU":
            play_won_lost = WON
            comp_won_lost = LOST
            winner = "AQ"

        elif comp_sel == "SW":
            play_won_lost = LOST
            comp_won_lost = WON
            winner = "SW"
    
    elif usr_sel == "HU":
        if comp_sel == "AQ":
            play_won_lost = LOST
            comp_won_lost = WON
            winner = "AQ"

        elif comp_sel == "SW":
            play_won_lost = WON
            comp_won_lost = LOST
            winner = "HU"

    elif usr_sel == "SW":
        if comp_sel == "AQ":
            play_won_lost = WON
            comp_won_lost = LOST
            winner = "SW"

        elif comp_sel == "HU":
            play_won_lost = LOST
            comp_won_lost = WON
            winner = "HU"

    # display computer selection:
    print(F"The computer randomly selected: {comp_sel}\n")
    # Display different print statement depending on which character won
    if winner == "AQ":
        print("Aqua Man extinguishes Human Torch")
    elif winner == "HU":
        print("Human Torch burns Swamp Thing")
    elif winner == "SW":
        print("Swamp Thing drowns Aqua Man")

    # Final print to reiterate what user choice and what comp chose, with win/lose status for each included.
    print(f"You chose {usr_sel} and the computer selected {comp_sel} so you've {play_won_lost} and the computer has {comp_won_lost}!")
        

main()

    

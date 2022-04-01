# File:    ForbesMenu.py 
# Project: CSIS2101 Assignment 7
# Author:  Matthew Forbes 
# History: Version 1.1 March 7, 2022

'''
The point of this program is to provide a menu for the user, asking them to select which planet they would like to
calculate the weight of a given 3D object's mass in pounds, into Newtons. Planets include Earth, Mars, the Moon, and
Jupiter.

The program will then present the following menu of selections: 
1.	Weight of an object in Newtons on Earth. 
2.	Weight of an object in Newtons on Mars. 
3.	Weight of an object in Newtons on Moon.
4.	Weight of an object in Newtons on Jupiter.
5.	Exit the program.

The menu selection will be validated, as will the weight provided in pounds (must be greater than 0). If an invalid 
menu option is input by user, the program will display an error message.
After input weight is validated, it is converted to kilograms and then passed as an argument to the appropriate planet's 
function. 
'''

import sys
import forbesWeights

def menuMatt():
    print("\nMENU")
    print("Please select one of the following options: ")
    print("1. Weight of an object in Newtons on Earth.")
    print("2. Weight of an object in Newtons on Mars.")
    print("3. Weight of an object in Newtons on Moon.")
    print("4. Weight of an object in Newtons on Jupiter.")
    print("5. Exit the program.")


def validInput(input):
    if input <= 0:
        print("Invalid input")   
        return False 
    return True # could use else, but since input <= 0 is a boolean (either true or false only) it's not necessary
    # since if input is equal to or less than 0, False will be returned to calling function. If input is greater than 0
    # then program will fall through to return True


def main():

    planet = "" # declare a planet variable that is an empty string so that the scope will be the entire function, instead of 
    # just an if statement for signficant print statement at bottom. Also allows it to be used in the planet select f-string short cut below.
    choice = 0 # declare choice variable for menu and set to 0 to enter first iteration of while loop below
    mass_prompt = "Please enter the object's mass in pounds: " # Another shortcut for repeated statements.
    LBS_PER_KG = 2.2 # Constant for self-documenting code, to avoid hard code errors, and convenience
    obj_mass_lbs = 0.0 # Create in scope of function for use below if statements inside while loop

    while choice != 5: # While choice is not equal to 5, this while loop woll be executed. It will always be executed at least once due
        # to assigning 0 to choice above.
        menuMatt() # Call the menu function to display the menu options

        choice = int(input("\nPlease enter one of the above choices (1 through 5): ")) # prompt user to choose a menu option and assign input to choice as an int
        while choice < 1 or choice > 5: # While choice is less than one or greater than 5 enter while loop
            choice = int(input("Invalid input, please enter one of the above numbers (1 through 5): ")) # indicate invalid input to user and prompt for valid input
            # this will continue to loop until a valid menu option is selected.

        if choice == 1: # if choice is equal to 1
            planet = "Earth" # assign planet to "Earth" for significant print statement below
            print(f"We are going to calculate the weight of the object on {planet}") # indicate to user which planet will be used in the calculations

            obj_mass_lbs = float(input(mass_prompt)) # prompt user to enter the object's mass in pounds and assign it to obj mass lbs
            while validInput(obj_mass_lbs) == False: # while obj_mass_lbs is invalid (validInput returns false):
                obj_mass_lbs = float(input(mass_prompt)) # prompt user for new mass in pounds and reassign to variable. Variable will be tested again and this process
                # will loop until False is not returned (only other option is true)

            mass_kg = obj_mass_lbs / LBS_PER_KG # calculate the object mass in kg by dividing mass in lbs by constant (2.2)
            newtons = forbesWeights.weightEarthMatt(mass_kg) # Call function from imported program to calculate the weight in Newtons based on the provided mass in kg
            # assign returned result to newtons for significant print statement below.


        elif choice == 2:
            # if choice is equal to 2
            planet = "Mars" # assign planet to "Mars" for significant print statement below
            print(f"We are going to calculate the weight of the object on {planet}") # indicate to user which planet will be used in the calculations

            obj_mass_lbs = float(input(mass_prompt)) # prompt user to enter the object's mass in pounds and assign it to obj mass lbs
            while validInput(obj_mass_lbs) == False: # while obj_mass_lbs is invalid (validInput returns false):
                obj_mass_lbs = float(input(mass_prompt)) # prompt user for new mass in pounds and reassign to variable. Variable will be tested again and this process
                # will loop until False is not returned (only other option is true)

            mass_kg = obj_mass_lbs / LBS_PER_KG # calculate the object mass in kg by dividing mass in lbs by constant (2.2)
            newtons = forbesWeights.weightMarsMatt(mass_kg) # Call function from imported program to calculate the weight in Newtons based on the provided mass in kg
            # assign returned result to newtons for significant print statement below.

        
        elif choice == 3:
            # if choice is equal to 3
            planet = "Moon" # assign planet to "Moon" for significant print statement below
            print(f"We are going to calculate the weight of the object on {planet}") # indicate to user which planet will be used in the calculations

            obj_mass_lbs = float(input(mass_prompt)) # prompt user to enter the object's mass in pounds and assign it to obj mass lbs
            while validInput(obj_mass_lbs) == False: # while obj_mass_lbs is invalid (validInput returns false):
                obj_mass_lbs = float(input(mass_prompt)) # prompt user for new mass in pounds and reassign to variable. Variable will be tested again and this process
                # will loop until False is not returned (only other option is true)

            mass_kg = obj_mass_lbs / LBS_PER_KG # calculate the object mass in kg by dividing mass in lbs by constant (2.2)
            newtons = forbesWeights.weightMoonMatt(mass_kg) # Call function from imported program to calculate the weight in Newtons based on the provided mass in kg
            # assign returned result to newtons for significant print statement below.


        elif choice == 4:
            # if choice is equal to 4
            planet = "Jupiter" # assign planet to "Jupiter" for significant print statement below
            print(f"We are going to calculate the weight of the object on {planet}") # indicate to user which planet will be used in the calculations

            obj_mass_lbs = float(input(mass_prompt)) # prompt user to enter the object's mass in pounds and assign it to obj mass lbs
            while validInput(obj_mass_lbs) == False: # while obj_mass_lbs is invalid (validInput returns false):
                obj_mass_lbs = float(input(mass_prompt)) # prompt user for new mass in pounds and reassign to variable. Variable will be tested again and this process
                # will loop until False is not returned (only other option is true)

            mass_kg = obj_mass_lbs / LBS_PER_KG # calculate the object mass in kg by dividing mass in lbs by constant (2.2)
            newtons = forbesWeights.weightJupiterMatt(mass_kg) # Call function from imported program to calculate the weight in Newtons based on the provided mass in kg
            # assign returned result to newtons for significant print statement below.


        elif choice == 5:
            print("\nGood Bye! All weights have been calculated.")
            sys.exit() # Exit program to avoid unitiated variable errors.

        
        print(f"The weight of the object with a mass of {obj_mass_lbs} pounds is {newtons:.2f} Newtons on {planet}.")


main()

        
















if __name__ == '__main__':
    main()

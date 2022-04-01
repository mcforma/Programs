# File:    MatthewC2F.py 
# Project: CSIS2101 Assignment 2
# Author:  Matthew Forbes 
# History: Version 1.1 January 20, 2022

''' 
The function of this program is to receive the temperature in degrees Celsius from
the user, which is then casted and assigned to a variable and converted to degrees
Fahrenheit. The original temperature (in Celsius) and the new temperature (in Fahrenheit)
are both displayed to the console for the user in a helpful message.
'''

# define program inside indented block in main function
def main():

    # Greeting
    print("Hello, I will convert Celsius to Fahrenheit for you.")

    # user is prompted to input the temperature in degrees Celsius via the keyboard
    # which is cast to a float and then assigned to the variable "matthewCel"
    matthewCel = float(input("Please enter the temperature in degrees Celsius: "))
    
    # Use supplied Celsius (matthewCel) in forumula to convert to Fahrenheit
    # Assign result to "forbesCel" variable.
    forbesCel = matthewCel * 9 / 5 + 32

    # Output meaningful message + result
    print(f"{matthewCel} degrees Celsius is {forbesCel:.3f} degrees Fahrenheit.")

main()
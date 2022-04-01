# File:    MatthewF2C.py 
# Project: CSIS2101 Assignment 2
# Author:  Matthew Forbes 
# History: Version 1.1 January 20, 2022

''' 
The function of this program is to receive the temperature in degrees Fahrenheit from
the user, which is then casted and assigned to a variable and converted to degrees
Celsius. The original temperature (in Fahrenheit) and the new temperature (in Celsius)
are both displayed to the console for the user in a helpful message.
'''

# define program inside indented block in main function
def main():
    
    # Greeting
    print("Hello, I will convert degrees Fahrenheit to degrees Celsius for you.")

    # user is prompted to input the temperature in degrees Fahrenheit via the keyboard
    # which is cast to a float and then assigned to the variable "matthewFar". 
    matthewFar = float(input("Please enter the temperature in degrees Fahrenheit: "))
    
    # Use supplied Fahrenheit (matthewFar) in forumula to convert to Celsius
    # Assign result to "forbesFar" variable.
    forbesFar = (matthewFar - 32) * 5 / 9

    # Output meaningful message + result
    print(f"{matthewFar} degrees Fahrenheit is {forbesFar:.3f} degrees Celsius.")

main()
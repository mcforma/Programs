# File:    AhsForbes.py 
# Project: CSIS2101 Assignment 6
# Author:  Matthew Forbes 
# History: Version 1.1 February 11, 2022

'''
1.	Write a function triangle_area_lastname (instead of main) that takes in the input of three sides of a triangle a, b and c 
as arguments into the function. 

2.	From triangle_area_lastname call the two functions given below which also takes a, b and c as function parameters. 

3.	Write a function is_valid that takes a,b and c as function parameters to test if the input is valid. This function returns 
true if sum of every two sides is greater than the third side. If input is not valid, returns false.

4.	If the is_valid function returns a false ask the user to input the sides again until the input is valid using a while loop.

5.	Once the input is valid call the function calc_Area that takes the valid a, b and c as function parameters which calculates 
the area of the triangle using semi perimeter (s) as shown in the formula given below and returns the area calculated. Display 
the area from the triangle_area_lastname using a meaningful print function. Area needs to be rounded to two decimals. 

 
6.	Math module should be used to find the square root. 
So when triangle_area_lastname ( 3,4,5 ) is called from the console. 
Program should print: 
“Area of triangle with sides 3,4 and 5 is 6.00 square inches.”. 

If triangle_area_lastname ( 3,4,9 ) is called:
Program prints. “Invalid input: Sum of any two sides has to be greater than the third side” and ask the user to input again until
valid sides are entered and area calculated.  

'''
import math

def triangle_area_forbes(a, b, c):

    # while is_valid with sides a, b, and c is equal to False, loop the following statements
    while is_valid(a, b, c) == False:
        print("Invalid input. Any two sides when summed must be greater than the third side, and non-negative.")
        # Use eval to get more than one variable input at a time. Inform user to separate with commas
        a, b, c = eval(input("Please input valid sides lengths separated by commas: "))

    # Once is_valid is equal to True, while loop will end and calc_Area is called with validated a, b and c sides with result 
    # assigned to area variable
    area = calc_Area(a, b, c)

    # Meaningful print statement with side lengths and area rounded to 2 decimals (since side lengths could technically be input
    # as floats with more than 2 decimal places)
    print(f"The area of a triangle with side lengths of {a:.2f}, {b:.2f}, {c:.2f} is: {area:.2f}")


# Check if input side lengths are valid by ensuring any two sides are greater than the third side
def is_valid(a, b, c):
    if a + b > c: # if a + b is greater than c, enter if block, if false, drop to next line, which is line 58, which returns False
        if a + c > b: # if a + c is also greater than b (in addition to a+b > c) enter if block. If false, drop to line 58 and return False
            if b + c > a: # if b + c is also greater than a in addition to two previous statements being true, return True. Otherwise, fall 
                # to next statement which is line 58, and return False
                return True
    return False


def calc_Area(a, b, c):
    semi_perimeter = (a + b + c) / 2 # semi perimeter formula using validated arguments

    # calculate area with semi perimeter formula
    area = math.sqrt(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))
    return area # return area to triangle_area_forbes to use in meaningful print statement

    



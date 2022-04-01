# File:    LoopsForbes.py 
# Project: CSIS2101 Assignment 4
# Author:  Matthew Forbes 
# History: Version 1.2 January 29, 2022

# Version History Notes: 
# 1.1: Initial program created and completed
# 1.2: Added additional comments to better relay thought process

"""
This program is designed to use a particular language feature, specifically loops in Python.
1. Create a method called loopsForbes with the following four loops. 

2. Write a loop that counts from 144 down to 131 , printing the count value each time in the 
loop. The output should be on one line look like this (144 143 142 141 140 139 138 137 136 
135 134 133 132 131). 

3. Write a loop that counts from 7 to 49 by sevens, printing the count in each iteration. 
The output should look like 7, 14, 21, 28, 35, 42, 49.  Notice the commas in between. Notice 
that there is no comma at the beginning or end. That means that you must do something special
either at the beginning or at the end. 

4. Ask the user to input an integer parameter The loop should count down only the even 
numbers, starting with the input number and ending with 0. For this you should use a while 
loop. The numbers should all appear on the same line. So for example if the input number 
passed is 10 (an even number) the output should be 

    10 8 6 4 2 0

So for example if the input number passed is 11 (an odd number) the output should be 
    10 8 6 4 2 0

5. Ask the user to input an integer parameter. The loop should count up all the odd numbers 
below the number, starting with the number 1 and up to the number that was passed as the 
input parameter. For this you should use a for loop.  The numbers should all appear on the 
same line. So for example if the number passed in using input is 7 the output should be 
    
    1 3 5 7

So for example if the number passed in using input is 8 the output should be 
    1 3 5 7

6. Name the file also as LoopsLastName.py with the loops function, do all these loops within 
the loopsLastname function. Do not submit 4 different programs. 

"""

# 1. Main Program
def loopsForbes():

    # 2. First Loop
    for i in range(144, 130, -1): # first number is starting number, second is limiter, last is step value 
        print(i, end=" ") # use end=" " to get space in between each iteration of printing i on same line

    # print newline escape character to get 2 new lines for next loop (one separating the outcomes)
    print("\n")

    # 3. Second Loop
    for val in range(7, 50, 7):
        if val != range(7, 50, 7)[len(range(7,50,7)) - 1]: # use last index of range. Could also simply hard code != 49
            # Could also assign the use the len() on range prior and assign to a variable like so: length = len(range(7,50,7))
            # and then do the index length - 1 (so: if val != range7,50,7)[length - 1]:). But that did not seem to be the
            # intended way to solve the problem.
            print(val, end=", ") # if val is not on last index of range, it will print the val with a comma and space
        else: # else normal print to get newline
            print(val)

    print()

    # 4. Third Loop
    num = int(input("Please enter an integer: ")) # Get input from user and cast to int and assign to num
    while num < 0: # Forces user to input at least 0 instead of negative integer so that there will be an output
        num = int(input("Please input a positive integer: "))

    while num >= 0: # while num is greater than or equal to 0
        if num % 2 == 0: # check if num is even via remainder
            print(num, end=" ") # if so, print the num and a space on same line
            num -= 2 #subtract two from counter to keep even. Could also subtract 1 but that would take longer
        else: # else subtract 1 and loop through again to test if even (which it will be)
            num -= 1

    print("\n")

    # 5. Fourth Loop
    num = int(input("Please input an integer: ")) # Get input from user, cast to int, assign to num variable.
    while num < 1:
        num = int(input("Please input an integer greater than or equal to 1: ")) # since output will be nothing if < 1 is input
    for i in range(1, num + 1, 2): # step by 2 
        if i % 2 == 1: # ensure number is odd
            print(i, end=" ") # print odd number with a space on same line  

loopsForbes()
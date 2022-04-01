# File:    Assgn5_Forbes.py 
# Project: CSIS2101 Assignment 5
# Author:  Matthew Forbes 
# History: Version 1.1 February 4, 2022

'''
1. Write a function that takes no parameters as input and the function should ask the user to 
enter a String and then prints “My favorite Video Game is vg.” where vg is the given input 
string. So if an user inputs Minecraft inside the function the output should look like:
My favorite Video Game is Minecraft. 

2. Write a function in Python that takes one parameter for the number of rows (n)  to display.
The input number of rows should be asked in the main and passed into the function as an 
argument. Using nested loops it should then display that many rows of percent signs, with 1 
percent sign in the first row, 2 percent signs in the second row, and so on and n-1 percent 
signs in the one before last row and n percent signs in the last row where n is the input 
number. The program should be able to run for any value of n. For example if n is entered as
5, there should be 5 lines printed out and there should be 1 percent sign in the first row, 
2 in the second, 3 in the third, 4 in the fourth and 5 percent sign in the last line.  A 
sample run would look like this where n = 5:

Enter number of rows: 5 ( Asked in main ) and the function prints out the following inside 
the function: ( Please note one space between each percent sign.)

3. Write a function to print the lyrics of our own version of the song “Old MacDonald”. One 
Stanza of the song is given below. As you know there are two more stanzas with a different 
animal and sound (instead of the cow and the moo). Your python program should print the 
lyrics for three different animals and their respective sounds using one function called 
three times, similar to the example verse below:

Write a function that takes two parameters ( strings) the animal name and the sound it makes 
to write one stanza.  Then this function should be called from main three times to write the 
whole lyrics. Here you call the function thrice with three different animals and their 
respective sounds and do not ask the user to input. Output will be the lyrics of the song 
with three stanzas. Please note the "" for the sound which should be in the output. 
'''

def main():
    # Call the 3 functions by names specified as instructed

    # 1.
    mattFavGame()

    # 2.
    n = int(input("Please enter the number of rows of percent signs to be displayed: "))
    while n <= 0:
        n = int(input("Please enter an integer that is equal to or greater than 1: "))
    mattPercentSign(n)

    # 3. Call function 3 times with different animal names and noises
    mattNurseryRhyme("cow", "moo")
    mattNurseryRhyme("pig", "oink")
    mattNurseryRhyme("sheep", "baah")

# 1. mattFavGame() (no parameters)
def mattFavGame():
    vg = input("Please enter your favorite Video Game name: ") # Get input from user and assign to vg
    print(f"My favorite Video Game is {vg}") # print out specified output with input from user
    print()


# 2. mattPercentSign() one parameter
def mattPercentSign(num):
    for row in range(0, num): # Iterable contains sequence 0 through num (n from main()). 
        # Each iteration, row variable is incremented by 1. This outer loop controls the number of rows.
        for col in range(row + 1): # Iterable contains sequence row + 1. Meaning col is assigned + 1
            # of whatever row is. So first iteration it is 1. Sequence is therefore 1 through num + 1
            # since row's limiter is num. This inner loop controls the number of columns. It will iterate 
            # row + 1 times, thereby printing "% " row + 1 times, before returning control to the outer loop.
            print("%", end=" ") # print % on the same line with a space separator. 
        print()
    print()


# 3. mattNurseryRhyme() two parameters
def mattNurseryRhyme(animal, noise):
    eieio = "E-I-E-I-O" # For convenience 
    oldCSIS = f"Old CSIS2101 had a function, {eieio}" # Convenience. Write once, use multiple times

    # Begin Stanza
    print(oldCSIS)
    print(f"And on his function he had a {animal}, {eieio}")
    print(f"With a \"{noise}-{noise}\" here and a \"{noise}-{noise}\" there") # \" is escape character for "
    print(f"Here a \"{noise}\" there a \"{noise}\"")
    print(f"Everywhere a \"{noise}-{noise}\"")
    print(oldCSIS)
    print()

main()
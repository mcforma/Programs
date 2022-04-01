# menu_demo.py
# Demo of a menu which does:
# Takes an integer input
# 1. Double the value
# 2. Squares the value
# 3. Finds the cube of the value
# 4. Finds the square root of the value
# 5. Exit (Quits the program)
import math

def display_menu():
    print("1. Double the value")
    print("2. Squares the value")
    print("3. Finds the cube of the value")
    print("4. Finds the square root of the value")
    print("5. Exit (Quits the program)")


def main():
    choice = 0

    while choice != 5:
        display_menu()
        choice = int(input("Please enter an option as a number from the menu: "))
        if choice == 1:
            double_number()
        elif choice == 2:
            square_number()
        elif choice == 3:
            cube_number()
        elif choice == 4:
            root_number()
        elif choice == 5:
            print("Good Bye, Exiting.....")
        else:
            print("Invalid input. Input has to be an integer between 1 and 5.\n")


def double_number():
    print("\nDoubles the number")
    num = int(input("Please enter a number: "))
    print(f"Double of the number {num} is {num * 2}\n")

    
def square_number():
    print("\nSquares the number")
    num = int(input("Please enter a number: "))
    print(f"Square of the number {num} is {num ** 2}\n")


def cube_number():
    print("\nCubes the number")
    num = int(input("Please enter a number: "))
    print(f"Cube of the number {num} is {num ** 3}\n")


def root_number():
    print("\nSquare root of the number")
    num = int(input("Please enter a number: "))
    print(f"Square root of the number {num} is {math.sqrt(num)}\n")


main()
        
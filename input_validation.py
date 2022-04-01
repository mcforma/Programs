# input_validation.py
# Ask user for a number. If number is between 1 and 100, you put print the number
# Or else, ask the user to enter the number again until it is between 1 and 100
# 1 and 100 are also valid values

def input_val():
    inp = int(input("Please enter a number between 1 and 100 including 100: "))

    while inp < 1 or inp > 100:
        print("Invalid input. Please enter again: ")
        inp = int(input("Please enter a number between 1 and 100 including 100: "))

    print(f"The number between 1 and 100 is: {inp}")

input_val()
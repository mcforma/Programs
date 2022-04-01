# Factor of 3 or 5
# Ask user to enter an integer
# If the given integer is a multiple of 3 or 5, print "Yes 3 and/or 5 is a factor"
# Else print "It is not a factor"
# For example, if input is 4, it should print "it is not a factor"
# and for input like 9, 15, etc. it should print The Yes statement.

def main():
    num = int(input("Please enter an integer: "))
    if num % 3 == 0 or num % 5 == 0:
        print(f"Yes, 3 and/or 5 is a factor of {num}.")
    else:
        print(f"{num} is not a multiple of 3 and/or 5.")

main()
# ifdemo2.py
# Demo of an if and elif loop

def main():
    x = int(input("Please enter an integer: "))
    # x = int(x)

    # If loop
    if x > 0:
        print(x , "Is a positive number.")
        print("So input is positive")
    elif x == 0:
        print("Input is 0.")
    else:
        print(x, "is negative")



main()
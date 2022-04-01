# ifdemo.py
# Demo of an if loop

def main():
    x = int(input("Please enter an integer: "))
    # x = int(x)

    # If loop
    if x > 0:
        print(x , "Is a positive number.")
    else:
        if x == 0:
            print("Input is 0.")
        else:
            print(x, "is negative")



main()


# even_odd_func_return.py
# A function to find whether a given input is an even number or an odd number

def main():
    num = int(input("Please enter an integer: "))

    ev = even_odd(num)

    if ev == True:
        print(f"{num} is EVEN.")
    else:
        print(f"{num} is ODD.")

def even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False

main()
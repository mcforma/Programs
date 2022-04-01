# square_odd.py
# Write a program that prints a value and its square for all odd numbers 1 through 10
# Use a for loop and a while loop to do this

def main():
    print("Number", "\t", "Square")
    num1 = 1

    while num1 <= 10:
        print(f"{num1} \t {num1 ** 2}")
        num1 += 2

    print("End of first while loop")

    for num2 in range(1,11,2):
        print(f"{num2} \t {num2 ** 2}")

    print("End of first for loop")

    # squares of odd numbers but in reverse order
    num3 = 10
    while num3 >= 1:
        if num3 % 2 == 1:
            print(f"{num3} \t {num3 ** 2}")
        num3 -= 1
    
    
    for num2 in range(9,0,-2):
        print(f"{num2} \t {num2 ** 2}")

main()
# squares.py
# Write a program that prints a value and its square from 1 through 10
# Use a for loop and a while loop to do this

def main():
    print("Number", "\t", "Square")
    num1 = 1

    while num1 <= 10:
        print(f"{num1} \t {num1 ** 2}")
        num1 += 1

    for num2 in range(1,11):
        print(f"{num2} \t {num2 ** 2}")

main()
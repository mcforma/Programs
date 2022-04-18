# Recursion explanation with factorial
# Factorial.py



def main():
    num = int(input("Please enter a positive integer: "))

    result = factorial(num)

    print(f"The factorial of {num} is {result}")


def factorial(n):

    if n == 0: 
        return 1
    else:
        return n * factorial(n - 1)

main()


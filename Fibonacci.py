# Fibonacci.py

# Recursion explanation with Fibonacci


def main():
    num = int(input("Please enter a positive integer: "))

    result = fibonacci(num)

    print(f"The fibonacci of {num} is {result}")


def fibonacci(n):

    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

main()


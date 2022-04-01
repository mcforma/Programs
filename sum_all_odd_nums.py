# sum all odd numbers between given inputs m and n including m and n if applicable

def main():
    m,n = eval(input("Please enter two positive integers separated by a comma and first one is small than the second one: "))

    while m >= n:
        print("Invalid input second number has to be greater than the first number")
        m,n = eval(input("Please enter two positive integers separated by a comma and first one is small than the second one: "))

    
    sumOddFor = 0
    
    for i in range(m,n+1):
        if i % 2 == 1:
            sumOddFor += i
    print(f"Sum of all odd numbers between {m} and {n} is {sumOddFor}")

    sumOddWhile = 0
    counter = m
    while counter <= n:
        if counter % 2 == 1:
            sumOddWhile += counter
        counter += 1

    print(f"Sum of all odd numbers between {m} and {n} is {sumOddFor}")

main()


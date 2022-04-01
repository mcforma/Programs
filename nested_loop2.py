def main():
    n = int(input("Please enter a positive number: "))

    for i in range(1, n+1):
        for g in range(0,i+1):
            print("%", end=" ")
        print()

main()

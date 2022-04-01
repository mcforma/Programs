# SumDemo_Input.py
# A program to find the sum of n numbers provided by user.

def main():
    sum_num = 0
    n = int(input("Please enter n so that we can calculate sum of n numbers: ")) # number of numbers to sum
    for num in range(1,n+1): # n+1 gives you n since the second number in range() is the exclusive end
        num = int(input(f"Please enter integer {num}: "))
        sum_num += num
    print(f"Sum of the given {n} numbers is {sum_num}")

main()
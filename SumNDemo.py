# SumDemo_Input.py
# A program to find the sum of n numbers.

def main():
    sum_num = 0
    n = int(input("Please enter n so that we can calculate sum of n numbers: ")) # number of numbers to sum
    for num in range(1,n+1): # n+1 gives you n since the second number in range() is the exclusive end
        sum_num += num
    print(f"Sum of first {n} numbers is {sum_num}")

main()
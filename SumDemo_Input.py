# SumDemo_Input.py
# A program to find the sum of 10 numbers from user.

def main():
    sum_num = 0
    for num in range(1,11):
        num = int(input(f"Please enter integer {num}: "))
        sum_num += num
    print(f"Sum of first 10 numbers is {sum_num}")

main()
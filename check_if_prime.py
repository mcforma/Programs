# check_if_prime.py
# This program determines if a user provided number is prime

def main():
    num = int(input("Please enter an integer to determine if it is prime: "))

    print(check_prime(num))

def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
main()
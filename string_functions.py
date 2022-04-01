# string_functions.py
# string functions that return a True or False

def main():
    sample = input("Please enter the string: ")

    if sample.isalnum():
        print(f"{sample} has only alphanumeric characters.")
    if sample.isalpha():
        print(f"{sample} has only alphabet characters")
    if sample.isdigit():
        print(f"{sample} has only digit/numbers")
    if sample.islower():
        print(f"{sample} has only characters in lowercase")
    if sample.isupper():
        print(f"{sample} has only characters in uppercase")

main()
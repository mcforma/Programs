# even_or_odd.py
# Program checks whether given number is even or odd

def even():
    num = int(input("Please enter an integer: "))

    evn = False
    if num % 2 == 0:
        evn = True
    else:
        evn = False

    # F string interpolation
    print(f"The input number {num} is even: {evn}")
    # normal string interpolation
    print("The input number", num, "is even:", evn)

even()
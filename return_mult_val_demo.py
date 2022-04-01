# return_mult_val_demo.py
# Program that returns multiple values

def main():
    # n1 = int(input("Please enther the first number: "))
    # n2 = int(input("Please enter the second number: "))
    n1, n2 = eval(input("Please enter two numbers separated by a comma: "))

    s, d, p, q = process_numbers(n1,n2)
    print(f"Two numbers: {n1} {n2}")
    print(f"Sum: {s}")
    print(f"Difference: {d}")
    print(f"Product: {p}")
    print(f"Ratio: {q:.2f}")


def process_numbers(x, y):
    sum_xy = x + y
    diff_xy = x - y
    prod_xy = x * y
    ratio_xy = x / y
    return sum_xy, diff_xy, prod_xy, ratio_xy

main()
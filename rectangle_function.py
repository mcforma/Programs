# rectangle_function.py
# To find the area of a rectangle and the perimeter of a rectangle.
# A = length * width
# P = 2.0 (length + width)

def main():
    length = float(input("Please enter the length of the rectangle: "))
    width = float(input("Please enter the width of the rectangle: "))

    calc_area(length, width)
    calc_perimeter(length, width)

def calc_area(l, w):
    area = l * w
    print(f"The area of a rectangle with a legnth of {l:0.2f} and a width of {w:0.2f} is {area:.2f}")

def calc_perimeter(l, w):
    perimeter = 2.0 * (l + w)
    print(f"The perimeter of a rectangle with length {l:.2f} and width {w:.2f} is {perimeter:2f}")

main()
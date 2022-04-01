# circle_function.py
# circle area and perimeter calculated using functions

PI = 3.14159

# main func gets radius and then calls calc_area and calc_perimeter funcs with radius as the argument
def main():
    radius = float(input("Please enter the radius of the circle: "))

    calc_area(radius)

    calc_perimeter(radius)

def calc_area(r):
    area = PI * r * r
    print(f"Area of the circle with radius {r} is {area}")

def calc_perimeter(rad):
    perimeter = 2 * PI * rad
    print(f"Circumference of the circle with radius {rad} is: {perimeter}")

main()
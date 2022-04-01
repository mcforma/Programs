# circle_function_return.py
# circle area and perimeter calculated using functions and returned

PI = 3.14159

# main func gets radius and then calls calc_area and calc_perimeter funcs with radius as the argument
def main():
    radius = float(input("Please enter the radius of the circle: "))

    ar = calc_area(radius)
    peri = calc_perimeter(radius)

    print(f"Circumference of the circle with radius {radius} is {peri:.02f}.")
    print(f"Area of the circle with radius {radius} is {ar:.02f}.")

def calc_area(r):
    area = PI * r * r
    return area

def calc_perimeter(rad):
    perimeter = 2 * PI * rad
    return perimeter

if __name__ == '__main__':
    main()
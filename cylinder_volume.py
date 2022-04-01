# cylinder_volume.py
# Calculate volume of a cylinder
# vol = pi * r * r * h  Where r is the radius of the cross section and h the height of the cylinder

import circle_function_return

def main():
    radius = float(input("Please enter the radius of the cylinder: "))
    height = float(input("Please enter the height of the cylinder: "))

    area = circle_function_return.calc_area(radius)

    vol = area * height

    print(f"Volume of the cylinder with radius: {radius}, and height {height} is {vol:.3f}")

if __name__ == '__main__':
    main()
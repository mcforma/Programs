# circle.py
# A program to calculate the area and circumference/perimeter of a cirlce.

# PI is defined here
PI = 3.14159

# radius of circle is assigned a value
# radius = 2.0

# Input done by user from console
radius = input("Please enter the radius of the circle: ")

# Input is always written as string, so it is casted/converted to float
radius = float(radius)

# calculating area of a circle
# area = PI * radius * radius
# Exponents are denoted by **
area = PI * radius**2

# calculating the perimeter or circumference of a circle
perimeter = 2 * PI * radius

# Displaying the area and perimeter
# print("Area of circle is:", area)
print(f"Area of circle is {area:.2f} with radius: {radius:.1f}")

#print("Circumference of the circle is:", perimeter)
print(f"Circumference of the circle is: {perimeter:^16.3f} with radius: {radius:.3f}")


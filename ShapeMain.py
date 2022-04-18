# ShapeMain.py
# Main file which uses the class Shape

import Shape
import math

def main():
    S1 = Shape.Shape("BLUE", 0.5)
    print(S1)

    R1 = Shape.Rectangle("PURPLE", 0.1, math.pi, 4.0)
    print(R1)

    C1 = Shape.Circle("WHITE", 0.3, 3.0)
    print(C1)

    compare_areas(R1, C1)

def compare_areas(s1, s2):
    if isinstance(s1, Shape.Shape):
        if isinstance(s2, Shape.Shape):
            if s1.calc_area() > s2.calc_area():
                print("First shape has a greater area")
            elif s1.calc_area() < s2.calc_area():
                print("Second shape has a greater area")
            else:
                print("Both shapes have the area.")
        else:
            print("Second object is not a shape.")
    else:
        print("First object is not a shape.")
        

main()
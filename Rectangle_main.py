#Rectangle_main.py
# This is where we create objects of the class, rectangle_class, and do the operations

import Rectangle

def main():
    rect1 = Rectangle.Rectangle(5.1, 2.9)

    print(rect1.get_length())
    print(rect1.calc_area())
    print(rect1.calc_perimeter())
    
    #print(rect1.__str__())
    rect2 = Rectangle.Rectangle(3.0, 2.0)
    print(rect2.__str__())

    rect2.set_length(99.0)

    rect2_area = rect2.calc_area()

    rect2_peri = rect2.calc_perimeter()

    print(f"Are of Rect2 is {rect2_area}")
    print(f"Perimeter of Rect2 is {rect2_peri}")
main()


# Circle_main2.py
# main to test your circle class

import CircleClass

def main():
    c1 = CircleClass.Circle(3.0)
    print(c1)

    c2 = CircleClass.Circle(2.0)
    print(c2)

    c3 = CircleClass.Circle(1.0)
    print(c3)

    circle_list = [c1, c2, c3]

    for circle in circle_list:
        print(circle.get_area())

main()
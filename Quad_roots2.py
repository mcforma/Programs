# Quad_roots2.py

# quad_roots.py
import math
'''
To find the quadratic roots of an equation of the form
a x^2 + b x + c = 0
where a b and c are constants

x = (-b +/- sqrt(b^2 - 4 a c)) / 2 a
'''

def main():
    print("This program solves quadratics.")
    a, b, c = eval(input("Please input 3 integers separated by a comma for \"a\", \"b\", and \"c\" respectively: "))
    quadroots(a,b,c)


def quadroots(a, b, c):
    disc = calc_disc(a,b,c)

    while disc < 0:
        print("Invalid input. The dsicriminant b*b - 4 * a * c is negative. Nonreal number.")
        a,b,c = eval(input("Please enter a,b,c for the quadratic equation separated by a comma: "))
        disc = calc_disc(a,b,c)

    dsc_root = math.sqrt(disc)

    if dsc_root == 0:
        root = -b/(2*a)
        print(f"Square root of the quadratic equation with {a}, {b}, {c} is {root}")
    else:
        root1 = (-b + dsc_root)/(2*a)
        root2 = (-b - dsc_root)/(2*a)
        print(f"Square root of the quadratic equation with {a}, {b}, {c} is {root1}, {root2}")

def calc_disc(a,b,c):
    return (b * b - 4 * a * c)
main()
    
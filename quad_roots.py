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
    disc = b * b - 4 * a * c

    if disc<0:
        return None

    dsc_root = math.sqrt(disc)

    root1 = (-b + dsc_root)/(2*a)
    root2 = (-b - dsc_root)/(2*a)

    print(f"Square root of the quadratic equation with {a}, {b}, {c} is {root1}, {root2}")

main()
    
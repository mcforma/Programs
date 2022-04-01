# File:    kilometer_converter.py
# Project: Programming Exercises Chapter 5
# Author:  Matthew Forbes 
# History: Version 1.1 February 8, 2022

def main():
    kilo = float(input("Please input a distance in kilometers: "))

    miles = Kilo_Converter(kilo)
    print(f"{kilo} kilometers is about {miles:.3f} miles (rounded to 3 decimal places)")


def Kilo_Converter(k_dist):
    m_dist = k_dist * 0.6214
    return m_dist

main()
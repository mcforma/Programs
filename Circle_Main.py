# Circle_Main.py
# Create Circle objects c1 and c2 using Circle_Class.py
# Week 12 Participation

import Circle_class

def main():

    #rad1 = float(input("Please enter the Circle's radius: ")) # get radius from user and assign to radius variable
    c1 = Circle_class.Circle(3.0) 
    # Create new Circle object with provided value from rad for the radius attribute

    print(c1.get_radius()) #print radius of c1
    print(c1.calc_area()) # print area of c1
    print(c1.calc_circum()) # print circumference of c1

    c1.set_radius(5.0) # set (mutate) radius of c1

    rad2 = float(input("Please enter the 2nd Circle's radius: ")) # get radius from user and assign to radius variable
    c2 = Circle_class.Circle(rad2) # Create new Circle object with provided value from rad for the radius attribute

    print(c2.get_radius()) # print radius of c2
    print(c2.calc_area()) # calculate area of c2
    print(c2.calc_circum()) # Print circumference of c2 

    c2.set_radius(8.0) # set (mutate) radius of c2

    
    print(c1.__str__()) 
    print(c2.__str__()) 



main()



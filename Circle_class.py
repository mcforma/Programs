# Circle_class.py
# Participation Question

# Create class called Circle similar to Rectangle.py
# Operations are: get_diameter, calc_area, calc_circum and __str__
# Do the main so that you can create two objects c1 and c2
# Include set function
# Make sure that files are submitted as individual files and DO NOT ZIP.

import math


class Circle:
    # The init function inializes the attributes of the class when a new instance of an object is created (akin to Constructor)
    def __init__(self, rad): # pass in self as required to be able to reference object as well as rad for radius attribute
        self.__radius = rad # assign the value from attribute rad to self radius as private (hence double underscore)

    
    # Get functions or Accessors
    def get_radius(self): # Get the radius of current object. Required to access private attribute as it cannot be accessed directly
        return self.__radius # 

    
    # Set functions or mutators
    def set_radius(self, r): # Mutate (change/modify) the radius with the input value in r
        self.__radius = r

    # Operations or Methods of the class
    def calc_area(self): # calculate area of circle and return to calling method
        return  math.pi * self.__radius * self.__radius

    def get_diameter(self): # Operation to get diameter
        return 2 * self.__radius

    def calc_circum(self): # Calculate circumference
        return 2 * math.pi * self.__radius

    def __str__(self):
        
        ret_str = f"Radius of Circle: {str(self.__radius)} \t Diameter of Circle: {str(self.get_diameter())}\n"
        ret_str += f"Area of Circle: {str(self.calc_area())} \t Circumference of Circle: {str(self.calc_circum())}"
        return ret_str

    




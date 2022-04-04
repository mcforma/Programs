#CircleClass.py
#Circle as a class
import math

class Circle:
    def __init__(self, rad):
        self.__radius = rad
        
    def get_radius(self): # accessor
        return self.__radius

    def set_radius(self, rd):
        self.__radius = rd


    # operations
    def get_diameter(self):
        return self.__radius * 2.0

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return math.pi * self.__radius * 2

    def __str__(self):
        ret_str = ""
        ret_str += "Radius of the circle: " + str(self.__radius) + "\n"
        ret_str += "Area of the circle: " + str(self.get_area()) + "\n"
        ret_str += "Perimeter of the circle: " + str(self.get_perimeter()) + "\n"
        ret_str += "Diameter of the circle: " + str(self.get_diameter()) + "\n"
        

        return ret_str
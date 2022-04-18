# Shape.py
# A class shape to demo inheritance
import datetime
import math

class Shape:
    def __init__(self, col, op):
        self.__color = col
        self.__opacity = op
        self.__crtdttm = datetime.datetime.now()

    # get functions (Accessors)
    def get_color(self):
        return self.__color

    def get_opacity(self):
        return self.__opacity

    def get_crttddtm(self):
        return self.__crtdttm

    # set functions (Mutators)

    def set_color(self, cr):
        self.__color = cr

    def set_opacity(self, o):
        self.__opacity = o

    def __str__(self):
        ret_str = ""
        ret_str += "Color of the shape is : " + self.__color + "\t" + " and Opacity is : " + str(self.__opacity * 100) + "%" 
        ret_str += "\tand created at: " + str(self.__crtdttm) + "\n"
        return ret_str

class Rectangle(Shape):
    def __init__(self, col, op, ln, wd):
        Shape.__init__(self, col, op)
        self.__length = ln
        self.__width = wd

     # Get functions or Accessors
    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width


    # Set functions or mutators
    def set_length(self, ln):
        self.__length = ln

    def set_width(self, wd):
        self.__width = wd
    
    # Operations or Methods of the class
    def calc_area(self):
        return self.__length * self.__width

    def calc_perimeter(self):
        perimeter = 2.0 * (self.__length + self.__width)
        return perimeter

    def __str__(self):
        ret_str = Shape.__str__(self)
        ret_str += "Length of Rectangle: " + str(self.__length) + "\t" + "Width of Rectangle: " + str(self.__width) + "\n"
        ret_str += "Area of Rectangle: " + str(self.calc_area()) + "\t" + "Perimeter of Rectangle: " + str(self.calc_perimeter()) + "\n"
        return ret_str


class Circle(Shape):
    def __init__(self, cl, op, rad):
        Shape.__init__(self, cl, op)
        self.__radius = rad
        

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
        ret_str = Shape.__str__(self)
        ret_str += "Radius of Circle: " + str(self.__radius) + "\t" + "Diameter of Circle: " + str(self.get_diameter()) + "\n"
        ret_str += "Area of Circle: " + str(self.calc_area()) + "\t" + "Circumference of Circle: " + str(self.calc_circum()) + "\n"
        return ret_str
    

    
    
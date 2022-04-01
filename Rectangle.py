# Rectangle.py
# Rectangle being programmed as a class.
# A class is an abstract concept (think blueprint) which has attributes and methods. An object is a particular instance of a class

class Rectangle:
    # This is the init function which initializes the attributes of the class (e.g. a Constructor)
    def __init__(self, ln, wd):
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
        ret_str = "Length of Rectangle: " + str(self.__length) + "\t" + "Width of Rectangle: " + str(self.__width) + "\n"
        ret_str += "Area of Rectangle: " + str(self.calc_area()) + "\t" + "Perimeter of Rectangle: " + str(self.calc_perimeter()) + "\t"
        return ret_str
    

    
    
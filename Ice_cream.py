# Ice_cream.py
# Define a class called icecream.

class Icecream:
    def __init__(self, br, fl,ty, wt):
        self.__brand = br
        self.__flavor = fl
        self.__type = ty
        self.__weight = wt

    # Gets or accessors (just gets/returns value)
    def get_brand(self):
        return self.__brand

    def get_flavor(self):
        return self.__flavor

    def get_type(self):
        return self.__type

    def get_weight(self):
        return self.__weight



    # Sets or mutators
    def set_brand(self, b):
        self.__brand = b

    def set_flavor(self, f):
        self.__flavor = f

    def set_type(self, t):
        self.__type = t

    def set_weight(self, w):
        self.__weight = w



    # operation or Method
    def get_price(self, cost_per_oz):
        if self.__flavor == "vanilla":
            price = cost_per_oz * self.__weight * 1

        elif self.__flavor == "chocolate":
            price = cost_per_oz * self.__weight * 1.2

        elif self.__flavor == "tresleeches":
            price = cost_per_oz * self.__weight * 1.5

        else:
            price = cost_per_oz * self.__weight * 1.6

        return price


    # Operations or Methods
    def eat(self):
        print(f"Ice cream of {self.__flavor} is being eaten")

    def __str__(self):
        ret_str = f"Ice cream of flavor {self.__flavor} sold by {self.__brand} weighs {str(self.__weight)} in a {self.__type}\n."
        return ret_str

    
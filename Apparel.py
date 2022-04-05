# File:    Apparel.py 
# Project: CSIS2101 Assignment 11
# Author:  Matthew Forbes 
# History: Version 1.1 April 4, 2022

class Apparel:
    def __init__(self, cost, weightInOunces, size, description): # Constructor for Apparel object. Include cost, weight (in oz) size and description attributes in addition to mandatory self
        self.__cost = cost # assign the instantiated object's cost to the cost that was passed into the Constructor
        self.__weightInOunces = weightInOunces
        self.__size = size
        self.__description = description
        self.__quantity = 1

    # Acessors 
    def get_cost(self):
        return self.__cost

    def get_weightInOunces(self):
        return self.__weightInOunces

    def get_size(self):
        return self.__size

    def get_description(self):
        return self.__description

    def get_quantity(self):
        return self.__quantity

    
    # Mutators
    def set_cost(self, price):
        self.__cost = price

    def set_weightInOunces(self, wt):
        self.__weightInOunces = wt

    def set_size(self, sz):
        self.__size = sz

    def set_description(self, descrpt):
        self.__description = descrpt

    def set_quantity(self, qty):
        self.__quantity = qty


    # Operations
    def get_order_cost(self):
        return self.__cost * self.__quantity

    def get_order_weight_in_ounces(self):
        return self.__weightInOunces * self.__quantity

    
    # str 
    def __str__(self):
        ret_str = "" # initialize return string to empty string
        ret_str += "$" + str(self.get_cost()) + " each for " + str(self.get_quantity()) + " " + str(self.get_size()) + " " + str(self.get_description()) + "."
        return ret_str
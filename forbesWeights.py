# File:    forbesWeights.py 
# Project: CSIS2101 Assignment 7
# Author:  Matthew Forbes 
# History: Version 1.1 March 7, 2022

'''
The point of this program is to calculate the weight of an object in Newtons, given the objects mass in kilograms.
The weight of the object will be calculated in Newtons on different planets like Earth, Mars, the Moon and Jupiter.
'''


# define weightEarthMatt function which takes one argument (object mass in KG)
def weightEarthMatt(obj_mass_KG):
    GRAVITY_ACCEL_RATE = 9.81 # Declare the Earth's gravitational acceleration as a constant
    earth_newtons = obj_mass_KG * GRAVITY_ACCEL_RATE # weight in newtons on Earth = mass in KG * Earth's gravitational acceleratation
    return earth_newtons # return the calculated newtons to calling function to be caught by variable for meaningful output


# define weightMarsMatt function which takes one argument (object mass in KG)
def weightMarsMatt(obj_mass_KG):
    GRAVITY_ACCEL_RATE = 3.77 # Declare Mars' gravitational acceleration as a constant
    mars_newtons = obj_mass_KG * GRAVITY_ACCEL_RATE # weight in newtons on Mars = mass in KG * Mars' gravitational acceleratation
    return mars_newtons # return the calculated newtons to calling function to be caught by variable for meaningful output


# define weightMoonMatt function which takes one argument (object mass in KG)
def weightMoonMatt(obj_mass_KG):
    GRAVITY_ACCEL_RATE = 1.62 # Declare the Moon's gravitational acceleration as a constant
    moon_newtons = obj_mass_KG * GRAVITY_ACCEL_RATE # weight in newtons on Moon = mass in KG * Moon's gravitational acceleratation
    return moon_newtons # return the calculated newtons to calling function to be caught by variable for meaningful output


# define weightJupiterhMatt function which takes one argument (object mass in KG)
def weightJupiterMatt(obj_mass_KG):
    GRAVITY_ACCEL_RATE = 25.95 # Declare Jupiter's gravitational acceleration as a constant
    jupiter_newtons = obj_mass_KG * GRAVITY_ACCEL_RATE # weight in newtons on Jupiter = mass in KG * Jupiter's gravitational acceleratation
    return jupiter_newtons # return the calculated newtons to calling function to be caught by variable for meaningful output



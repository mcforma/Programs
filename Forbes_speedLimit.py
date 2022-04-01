# File:    Forbes_speedLimit.py 
# Project: CSIS2101 Assignment 3
# Author:  Matthew Forbes 
# History: Version 1.3 January 25, 2022

"""
This program is desisgned to calculate the amount a driver should be fined for speeding,
depending upon how many miles per hour over the speed limit they are going, and to provide
an output including the speed limit, the speed of the driver, whether it was a school zone,
the total fine amount, and one of a few predefined messages to the driver, depending on which
condition is met. This is accomplished using the if, elif, else decision structure, in addition
to receiving the speed limit and speed of the driver as input from the user. It is assumed that
the other variables are allowed to be used in addition to those provided in the assignment 
instructions. In the event that additional variables are not allowed, another solution using only
the three provided variables is provided below in a commented out section. 
"""

import sys

def Forbes_SpeedLimit():

    # get zone's speed limit from user
    matt_speedLimit = float(input("Please input the speed limit of the zone: "))

    # get speed of driver's vehicle from user
    matt_speed = float(input("Please input the speed of the vehicle: "))

    # get if speeding occurred in school zone from user
    if matt_speed - matt_speedLimit > 0: # added this in order to prevent it from outputting if driver
        # was not speeding
        matt_s_zone = input("Did the speeding occur in a school zone? Please only enter \"yes\" or \"y\"" +
        " for yes, or \"no\" or \"n\" for no. Any other input will be considered \"yes\": ")

        # if input is not "yes", "y", "no", or "n", user is informed input is invalid
        # and school zone variable is assigned string literal "yes"
        # Accordingly nested this if statement inside the above in the even that the driver is not speeding
        # to prevent error
        if matt_s_zone != "yes" and matt_s_zone != "y" and matt_s_zone != "no" and matt_s_zone != "n":
            print("That input is invalid and will be considered as \"yes\" or \"y\".")
            matt_s_zone = "yes"

    # if more variables are allowed
    # Get speeding amount (MPH over speed limit), assign to variable and
    # use that amount to get corresponding information from instructions
    speeding_amount = matt_speed - matt_speedLimit
    if speeding_amount <= 0:
        print(f"Speed Limit: {matt_speedLimit}")
        print(f"Vehicle Speed: {matt_speed}")
        sys.exit("You are a good Driver.") # Exit the program early if the driver is not speeding to
        # save resources and prevent error due to use of uninitiated variables
    
    elif speeding_amount < 10 and speeding_amount > 0:
        fine_amount = 69.50
        message = "Slow down!"
    elif speeding_amount < 20:
        fine_amount = 99.50
        message = "Drive with caution!"
    elif speeding_amount < 30:
        fine_amount = 129.50
        message = "You are in danger zone!"
    elif speeding_amount < 35:
        fine_amount = 149.50
        message = "You are over speeding!"
    elif speeding_amount >= 35:
        fine_amount = "Court Mandatory - Fine decided in Court"
        message = "See you in Court!"

    if speeding_amount < 35 and speeding_amount > 0:
        if matt_s_zone == "yes" or matt_s_zone == "y":
            fine_amount *= 2

    print(f"\nSpeed Limit: {matt_speedLimit}")
    print(f"Vehicle Speed: {matt_speed}")
    print(f"School zone: {matt_s_zone}")
    if type(fine_amount) == str:
        print(f"Fine: {fine_amount}")
    else:
        print(f"Total fine calculated: ${fine_amount:.2f}")
    print(f"Display: {message}")


    # If the only variables allowed are the three provided in instructions
    """ # Driver is driving within speed limit
    if matt_speed - matt_speedLimit <= 0:
        print(f"Speed Limit: {matt_speedLimit}")
        print(f"Vehicle Speed: {matt_speed}")
        print(f"You are a good Driver.")

        
    # if vehicle speed over limit is less than 10 and greater than 0
    elif matt_speed - matt_speedLimit < 10 and matt_speed - matt_speedLimit > 0:
        print(f"\nSpeed Limit: {matt_speedLimit}")
        print(f"Vehicle Speed: {matt_speed}")
        print(f"School zone: {matt_s_zone}")

        # if speeding in school zone, fine is doubled
        if matt_s_zone == "yes" or matt_s_zone == "y":
            print(f"Total fine calculated: ${69.50 * 2}")
        elif matt_s_zone == "no" or matt_s_zone == "n":
            print(f"Total fine calculated: $69.50")
        # Display
        print("Slow Down!")


    # if vehicle speed over limit is less than 20
    elif matt_speed - matt_speedLimit < 20:
        print(f"\nSpeed Limit: {matt_speedLimit}")
        print(f"Vehicle Speed: {matt_speed}")
        print(f"School zone: {matt_s_zone}")

         # if speeding in school zone, fine is doubled
        if matt_s_zone == "yes" or matt_s_zone == "y":
            print(f"Total fine calculated: ${99.50 * 2}")
        elif matt_s_zone == "no" or matt_s_zone == "n":
            print(f"Total fine calculated: $99.50")
        # Display
        print("Drive with caution!")


    # if vehicle speed over limit is less than 30
    elif matt_speed - matt_speedLimit < 30:
        print(f"\nSpeed Limit: {matt_speedLimit}")
        print(f"Vehicle Speed: {matt_speed}")
        print(f"School zone: {matt_s_zone}")

        # if speeding in school zone, fine is doubled
        if matt_s_zone == "yes" or matt_s_zone == "y":
            print(f"Total fine calculated: ${129.50 * 2}")
        elif matt_s_zone == "no" or matt_s_zone == "n":
            print(f"Total fine calculated: $129.50")
        # Display
        print("You are in danger zone!")

    # if vehicle speed over limit is less than 35
    elif matt_speed - matt_speedLimit < 35:
        print(f"\nSpeed Limit: {matt_speedLimit}")
        print(f"Vehicle Speed: {matt_speed}")
        print(f"School zone: {matt_s_zone}")
        
        # if speeding in school zone, fine is doubled
        if matt_s_zone == "yes" or matt_s_zone == "y":
            print(f"Total fine calculated: ${149.50 * 2}")
        elif matt_s_zone == "no" or matt_s_zone == "n":
            print(f"Total fine calculated: $149.50")
        # Display
        print("You are over speeding!")


    # if vehicle speed over limit is 35 MPH or greater
    elif matt_speed - matt_speedLimit >= 35:
        print(f"\nSpeed Limit: {matt_speedLimit}")
        print(f"Vehicle Speed: {matt_speed}")
        print(f"School zone: {matt_s_zone}")
        print("Total Fine Calculated = Court Mandatory - Fine decided in Court")
        print("See ya in court!")"""

Forbes_SpeedLimit()
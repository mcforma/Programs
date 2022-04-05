# File:    MattOrderReceipt.py 
# Project: CSIS2101 Assignment 11
# Author:  Matthew Forbes 
# History: Version 1.1 April 4, 2022

import Apparel

def main():

    dTotalCost = 0.0 # initialize variable for total cost of all apparel items to 0.0
    iTotalWeight = 0 # initialize variable for total weight of all apparel items to 0

    # Put the 4 apparels being ordered in apparel1 through apparel4
    apparel1 = Apparel.Apparel(18.99, 27, "Large", "Denim Jacket") # Create Apparel object by using the program (module) name and then the class name. Supply necessary attributes in order
    apparel2 = Apparel.Apparel(9.49, 15, "Medium", "Track Pants")         
    apparel3 = Apparel.Apparel(109.99, 35, "Small", "Cashmere Sweater")         
    apparel4 = Apparel.Apparel(5.49, 7, "X-Large", "Woolen Socks") 

    apparel2.set_quantity(3) # mutate default quantity from default (1) to 3 for apparel2
    apparel4.set_quantity(2) # mutate default quantity from default (1) to 2 for apparel4

    apparel_list = [apparel1, apparel2, apparel3, apparel4] # Initialize list with Apparel objects

    print("Here are your shopping cart contents. ")

    # for each apparel in list:
    for apparel in apparel_list:
        print(apparel) # Calls __str__ which returns the ret_str to the print function
        dTotalCost += apparel.get_order_cost()  # Sum equals apparel's order cost and each successive apparel order's cost to get total cost of all four apparel orders (since list contains four elements)
        iTotalWeight += apparel.get_order_weight_in_ounces() # Sum equals apparel's weight in oz and each successive apparel order's weight in oz to get total weight of all four apparel orders (since list contains four elements)

     # Show order details        
    print(f"The cost of your order is ${dTotalCost:0.2f}.") # display total order cost for all apparel in signficant print statement
    print(f"The shipping weight is {iTotalWeight // 16} pounds {iTotalWeight % 16} ounces.") # display total shipping weight for all apparel in pounds and ounces in signficant print statement

if __name__ == "__main__": 
    main()

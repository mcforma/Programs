# File:    pain_job_estimator.py 
# Project: Starting Out with Python
# Author:  Matthew Forbes 
# History: Version 1.1 February 9, 2022

def main():
    sq_ft = float(input("Please enter the square feet of wall space to be painted: "))
    paint_price_per_gallon = float(input("Please enter the paint price per gallon: $"))

    numGallons, paintCost = calc_num_gallons_cost(sq_ft, paint_price_per_gallon)
    laborHours, laborCost = labor_hours_cost(sq_ft)

    total_cost = laborCost + paintCost

    print(f"Gallons required: {numGallons}")
    print(f"Hours of labor required: {laborHours}")
    print(f"Cost of paint: {paintCost}")
    print(f"Labor cost: {laborCost}")
    print(f"Total cost of paint job: {total_cost}")
    

def calc_num_gallons_cost(sqFt, pricePerGal):
    num_gallons = sqFt / 112
    paint_cost = num_gallons * pricePerGal
    return (num_gallons, paint_cost)

def labor_hours_cost(sqFt):
    FT_PAINTED_PER_HOUR = 112 / 8 # 14 feet per hour. 112 feet takes 8 hours
    HOURLY_LABOR_COST = 35.0

    job_hours = sqFt / FT_PAINTED_PER_HOUR
    labor_cost = job_hours * HOURLY_LABOR_COST

    return(job_hours, labor_cost)

main()
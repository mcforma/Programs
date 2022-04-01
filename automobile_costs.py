# File:    automobile_costs.py
# Project: Programming Exercises Chapter 5
# Author:  Matthew Forbes 
# History: Version 1.1 February 8, 2022

def main():
    print("This program calculates the monthly and annual automobile expenses.")
    monthly_loan = float(input("Please enter the monthly cost for your loan: "))
    monthly_insurance = float(input("Please enter the monthly cost of car insurance: "))
    monthly_gas = float(input("Please enter the monthly cost of gas: "))
    monthly_oil = float(input("Please enter the monthly oil change cost: "))
    monthly_tires = float(input("Please enter the monthy tire cost: "))
    monthly_maint = float(input("Please enter the monthly maintenance cost: "))

    monthly_auto_cost = calc_monthly_auto_cost(monthly_loan, monthly_insurance, monthly_gas, monthly_oil, monthly_tires, monthly_maint)
    yearly_auto_cost = calc_yearly_auto_cost(monthly_loan, monthly_insurance, monthly_gas, monthly_oil, monthly_tires, monthly_maint)

    print(f"Total monthly auto expenses are: ${monthly_auto_cost:.2f}")
    print(f"Total yearly auto expenses are: ${yearly_auto_cost:.2f}")



def calc_monthly_auto_cost(m_loan, m_insur, m_gas, m_oil, m_tire, m_maint):
    total_monthly = m_loan + m_insur + m_gas + m_oil + m_tire + m_maint
    return total_monthly

def calc_yearly_auto_cost(y_loan, y_insur, y_gas, y_oil, y_tire, y_maint):
    NUM_MONTHS_IN_YEAR = 12
    total_yearly = (y_loan + y_insur + y_gas + y_oil + y_tire + y_maint) * 12
    return total_yearly

main()
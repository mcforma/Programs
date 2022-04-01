# date.py
'''
A date is given in the format mm/dd/yyyy. This needs to be translated to the format 
month day, year
For example, if the user enters 1/1/2022
Output should be January 1, 2022
'''

def main():
    date = input("Please enter a date in mm/dd/yyyy format: ")

    date_list = date.split("/")

    months = ["January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"]

    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])

    actual_month = months[month-1]

    print(f"The date is {actual_month} {day}, {year}")

main()



    

        
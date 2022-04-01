# input: a given year
# Ouput check whether the given year is a leap year or not.
# The function should take the year as an input and return a True if the year is leap year and return
# False if not a leap year

# If the year is not divisible by 4, its not a leap year
#But if divisible by 4, check whether the year is divisble by 100 and if yes,
# Checl whether the year is divisble by 400 and then its a leap year
# and if not divisble by 100 it is a leap year. 2000 is a leap year, nut 2100 is not.

def main():
    year = int(input("Please enter a year: "))
    is_valid = is_leap_year(year)

    if is_valid == True:
        print(f"{year} is a LEAPYEAR.")
    else:
        print(f"{year} is not a LEAPYEAR.")


def is_leap_year(yr):
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False
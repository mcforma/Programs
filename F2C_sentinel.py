#F2C_sentinel.py
#We are converting a set of temperatures from Farenheit to Celsius

def main():
    inp = input("Do you have a temperature to convert from Farenheit to Celsius? Say yes to continue: ")
    
    while inp == "yes":
        fahr = float(input("Please enter a temperature in Farenheit: "))

        celsius = (fahr -32) * 5 / 9

        print(f"{fahr} in Farenheit is equivalent to {celsius} in celsius.")

        inp = input("Do you have a temperature to convert from Farenheit to Celsius? Say yes to continue: ")

main()
# calc_restaurant_bill.py

def main():
    amount = float(input("Please enter the total amount before tax: "))

    calc_tax(amount, 9.0)

def calc_tax(amount, tax=7.5):
    total_amount = amount * (1 + tax/100)
    print(f"You have to pay ${total_amount:.2f}")

main()
# String return demo

def main():
    temp = float(input("Please enter the temperature for the day in Farenheit: "))

    msg = weather(temp)
    print(msg)



def weather(t):
    if t > 100:
        message = "It's Arizona weather"
    elif t > 90:
        message = "It's Florida weather"
    elif t > 80:
        message = "It's California weather"
    elif t > 70:
        message = "It's Colorado weather"
    else:
        message = "It's Minnesota weather"
    return message

main()
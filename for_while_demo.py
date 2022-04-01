# for_while_demo.py
# Print numbers from 1 to 10 using a while loop and a for loop

def main():
    counter = 1
    while counter <= 5:
        print(f"counter = {counter}")
        counter += 1

    for val in range(3,7):
        print(val)
    
    for k in range(1,20,4):
        print(k)

    for val in [-1, 3, 5]:
        print(val)

main()
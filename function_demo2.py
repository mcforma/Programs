# function_demo2.py

def main():
    x = int(input("Please enter the lower value of the range: "))
    y = int(input("Please enter the upper limit of the range: "))

    sum_range(x,y)
    print("The function has been executed.")


def sum_range(m,n):
    sum_m_n = 0
    for num in range(m, n):
        sum_m_n += num
    print(f"Sum of numbers starting from {m} until {n} (n not included) is {sum_m_n}")

main()
main()
main()


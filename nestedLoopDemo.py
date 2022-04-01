# nestedLoopDemo.py
# nested loop is a repetition loop within a repetition loop
# print multiplication table 1 through 10

def main():
    print(f"1st number \t2nd number \tPRODUCT")
    for i in range(1,11):
        for j in range(1,11):
            print(f"{i}", "\t\t", f"{j}", "\t\t", f"{i*j}")

main()
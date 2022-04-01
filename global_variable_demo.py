# global_variable_demo.py
# demo of glaobal variables

birds = 4000 # global is keyword to declare global variable
def main():
    global birds
    birds = 4000

    print(f"Birds inside main: {birds}")

    birdTexas()
    print(f"Birds after Texas: {birds}")

    birdFlorida()
    print(f"Birds after Florida: {birds}")


def birdTexas():
    global birds 
    birds += 100
    print(f"Birds inside Texas: {birds}")

def birdFlorida():
    global birds 
    birds += 900
    print(f"Birds inside Florida: {birds}")

main()
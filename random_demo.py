# random_demo.py
# use of random library

import random
random.seed(10)

def main():
    flip = random.randint(1,100)
    print(flip)

    random1 = random.randrange(10, 20, 3)
    print(random1)

    random2 = random.random()
    print(random2)

    random3 = random.uniform(1,10)
    print(random3)


main()
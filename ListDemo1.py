# ListDemo1.py
# Demo of Lists

def main():
    numLists = [2, 3, 5, 7, 11, 13, 17, 19]
    fruitList = ["Apple", "Orange", "Blackberry", "Strawberry", "Guava", "Watermelon"]
    studentList = ["John Smith", "js1234@mynova.nsu.edu", 18, "(954)555 1234"]

    print(numLists)
    print(fruitList)

    fruitList[1] = "Peach"
    print(fruitList)

    print(len(numLists))
    print(len(fruitList))

    print(numLists[0])
    print(numLists[4])
    print(numLists[7])

    for fruit in fruitList:
        print(fruit)

    for num in range(len(numLists)):
        print(numLists[num])


    list3 = [ 1.1, 2.2, 3.3 ]
    print(list3)

    print(list3 * 3)

    print("Apple" in fruitList)
    print("Pear" in fruitList)

main()
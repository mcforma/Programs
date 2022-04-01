# list_functions_demo.py
# List functions demo

def main():
    fruitList = ["Apple", "Orange", "Blackberry", "Strawberry", "Guava", "Watermelon"]
    print(fruitList)

    fruitList[1] = "Peach"
    print(fruitList)

    fruitList.append("Orange")
    print(fruitList)

    fruitList.insert(3, "Pear")
    print(fruitList)

    fruitList.remove("Guava")
    print(fruitList)

    del fruitList[0]
    print(fruitList)



main()
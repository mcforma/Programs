# copy_list_demo.py
# Methods to copy a list

def main():
    list1 = [24, 33, 15, 79, 11]
    print(list1)

    list2 = list1 # Shallow copy. Lists are reference types, so List2 points to the same areas in memory on the heap that List 1 is,
    # so when list1 is changed, so is list2.
    print(list2)

    list1[2] = 75
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")

    list3 = []
    list3 += list1 # Deep copy via concatenation (append also works)
    print(f"List 3: {list3}")

    
    list4 = []
    for i in list1: # Deep copy via for loop and list append
        list4.append(i)
    print(f"List 4: {list4}")

    list5 = [item for item in list1] # Best deep copy method in Python

    list1[2] = 15

    print(list1)
    print(list2)
    print(list3)

    list4 = []
    for i in list1:
        list4.append

main()
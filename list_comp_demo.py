# list_comp_demo.py
# Examples of list comprehension

def main():

    list1 = [1, 2, 3, 4, 5, 6, 7]

    list2 = [item for item in list1] # Best deep copy method in Python

    print(list2)

    list3 = [item * item for item in list1]
    print(list3)

    list4 = [item for item in list1 if item < 5]
    print(list4)


    fruit_list = ["Apples", "Orange", "Cherry", "Watermelon"]
    print(fruit_list)

    len_list = [len(s) for s in fruit_list]
    print(len_list)

    names = [["Joe", "Kim"], ["Sam", "Sue"], ["Kelly", "Chris"]]

    print(names[0][0]) # [Row #][Column #]

    

main()

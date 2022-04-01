

from hashlib import new


def main():

    print("The program is provided two strings by the user. The first is the string proper. The second is the substring\n" +
    "which will be searched for in the first string. The second occurrence of the substring will have the index returned and\n" +
    "printed to the console. If there is only one (or zero) instances of the substring in the string, it will return -1.")

    orig = input("\nPlease input a string to search through for a specified substring: ") # prompt user for string and assign result to variable
    sub = input("Please enter the substring you are searching for: ") # prompt user for substring and assign to variable 

    second_inst_index = matthew_find(orig, sub)

    print(f"Index of second instance is: {second_inst_index}")


def matthew_find(orig, sub):
    index = orig.find(sub)
    if index == -1:
        return -1

    
    newString = orig[index + len(sub):]
    print(newString)


    if newString.find(sub) == -1:
        return -1
    else:
        print(index)
        index += len(sub) + newString.find(sub)
        return index

main()
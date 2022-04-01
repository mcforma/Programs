# File_input_demo5.py
# Demo of how to reaad from a file using a while loop and process data


def main():
    # Create a file object and open the input file

    inFile = open("super.txt", "r")
    # We did open a file with the file name specified and in "r" (read) mode

    line = inFile.readline()

    while line != "":
        name_list = line.split()
        print(name_list)
        first_name = name_list[0]
        last_name = name_list[1]
        user_id = first_name[0] + last_name
        print(user_id)
        print(line.strip("\n"))
        line = inFile.readline()


    inFile.close()

main()
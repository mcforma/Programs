# File_output_demo.py
# Demo of how to read from and write to a file using a while loop and process data


def main():
    # Create a file object and open the input file

    inFile = open("super.txt", "r")
    # We did open a file with the file name specified and in "r" (read) mode

    # A file object is created with mode = "w"rite
    oFile = open("userid.txt", "w")

    line = inFile.readline()

    while line != "":
        name_list = line.split()
        #print(name_list)
        first_name = name_list[0]
        last_name = name_list[1]
        user_id = first_name[0] + last_name
        print(user_id)
        print(line.strip("\n"))

        # Write command writes to the file
        oFile.write(user_id + "\n")

        line = inFile.readline()


    inFile.close()
    oFile.close()

main()
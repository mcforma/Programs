# File_process_rec.py
# How to modify a record in a file or delete a record

import os

def main():
    iFile = open("Menu.txt", "r")
    temp = open("temp.txt", "w")

    line = iFile.readline()
    found = False

    while line != "":
        if "Milk Shake" in line: # if "Milk Shake" is present in a line in Menu.txt, write "Orange Juice" instead
            temp.write("Orange Juice" + "\n") # in temp.txt
            found = True
        else: # else write the line as is into temp.txt
            temp.write(line)

        line = iFile.readline()

    iFile.close()
    temp.close()

    if found == True:
        os.remove("Menu.txt") # import os and remove "Menu.txt" from folder 
        os.rename("temp.txt.", "Menu.txt") # Rename "temp.txt" to "Menu.txt"
        print("File has been updated.")

    else:
        print("The item was not found in the file.")


main()
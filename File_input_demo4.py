# File_input_demo4.py
# Demo of how to read from a file



def main():
    # Create a file object and open the input file

    inFile = open("super.txt", "r")
    # We did open a file with the file name specified and in "r" (read) mode

    line = inFile.readline()

    while line != "":
        print(line.strip("\n"))
        line = inFile.readline()


    inFile.close()

main()
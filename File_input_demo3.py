# File_input_demo3.py
# Demo of how to read from a file



def main():
    # Create a file object and open the input file

    inFile = open("super.txt", "r")
    # We did open a file with the file name specified and in "r" (read) mode

    for line in inFile:
        print(line.strip("\n"))

    inFile.close()

main()
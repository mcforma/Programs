# File_input_demo2.py
# Demo of how to read from a file



def main():
    # Create a file object and open the input file

    inFile = open("super.txt", "r")
    # We did open a file with the file name specified and in "r" (read) mode

    line1 = inFile.readline()
    line2 = inFile.readline()
    line3 = inFile.readline()
    line4 = inFile.readline()
    line5 = inFile.readline()
    line6 = inFile.readline()

    print(line1.strip("\n"))
    print(line2.strip("\n"))
    print(line3.strip("\n"))
    print(line4.strip("\n"))
    print(line5.strip("\n"))
    print(line6.strip("\n"))

    
    

main()
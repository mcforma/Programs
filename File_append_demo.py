# File_append_demo.py
# How to append to the file




def main():
    inFile = open("super.txt", "a") # The mode here is append (to the end of the file)

    inFile.write("\nWonder Woman\n")

    inFile.close()

main()
# file_error.py
# FileNotFoundError

def main():
    iFile = open("CSIS.txt", "r")

    line = iFile.readline()

    while line != "":
        print(line + "\n")

    iFile.close()

main()
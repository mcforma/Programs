# File_input_numbers_input.py
# Demo of how to reaad from a file using a while loop and process data



def main():
    # Create a file object and open the input file

    inFile = open("numbers.txt", "r")
    # We did open a file with the file name specified and in "r" (read) mode

    line = inFile.readline()
    sum_numbers = 0
    counter = 0

    while line != "":
        counter += 1
        number_read = int(line)
        sum_numbers += number_read

        line = inFile.readline()

    if counter == 0:
        avg = 0
    else:
        print(f"Number of numbers in the file: {counter}")
        avg = sum_numbers / counter

    print(f"Average of numbers read in from file is: {avg}")

    inFile.close()

main()
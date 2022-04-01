

def main():

    inFile = open("decimals.txt", "r") # create input file object in "r"ead mode
    oFile = open("decimals_output.txt", "w") # create an output file object in "w"rite mode

    line = inFile.readline()
    sum_dec = 0
    counter = 0

    while line != "":
        counter += 1
        decimal_read = float(line)
        sum_dec += decimal_read 

        line = inFile.readline()

    if counter == 0:
        avg = 0

    else:
        print(f"Number of numbers in the file: {counter}")
        avg = sum_dec / counter

    print(f"Average of numbers read in from file is: {avg}")

    oFile.write("Average from numbers from decimals.txt: " + str(avg))

    inFile.close()
    #oFile.close()

main()


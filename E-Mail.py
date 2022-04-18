# hero_power_in_out_error.py
# Create a program that reads superhero names and their power from a file. There is only the hero name and power on each line.
# Take this data and write it along with " has special power of " (so "Superman HeatVision" would result in "Superman has special power of HeatVision")
# Include error handling in the event that the file is not found with a message printed to the user's console indicating such.

def main():

    try:
        inFile = open("mattssuper.txt", "r")
        oFile = open("forbespower.txt", "w")

        line = inFile.readline()

        while line != "":
            line = line.rstrip("\n") # DO NOT FORGET
            hero_list = line.split()

            hero = hero_list[0]
            power = hero_list[1]
            output_text = hero + " has special power of " + power
            oFile.write(output_text + "\n")

            line = inFile.readline()

        inFile.close()
        oFile.close()
        
    except IOError:
        print(f"An error ocurred trying to read mattssuper.txt")
        print("The file does not exist.")

main()

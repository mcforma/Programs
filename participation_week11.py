# participation_week11.py

# You are given a file of first names and last names like super.txt
# Create an output file of user ids created from the first file
# The condition is userid is first name first alphabet + last name
# But length of the userid should be less than or equal to five characters (so 4 only from last name)

def main():

    iFile = open("super.txt", "r")
    oFile = open("User ID (5 char).txt", "w")

    line = iFile.readline()

    while line != "":
        name_list = line.split()
        first_name = name_list[0]
        last_name = name_list[1]
        user_id = first_name[0] + last_name[0:4]
        user_id = user_id.rstrip()

        oFile.write(user_id + "\n")
        line = iFile.readline()

    iFile.close()
    oFile.close()

main()

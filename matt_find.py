# matt_find.py
# regular find finds the index of the first instance of a substring within a string
# For example "Mississippi".find("ss") gives the result 2 which is the first index of "ss"
# firstname_find.py finds the index of the second instance of the substring in the string
# "Mississippi".firstname_find("Mississippi","ss") returns 5
# firstname_find("Mississippi","i") returns 4 which is the index of the second i.
# If there is only one instance of the substring, then return -1
# Participation Question Week 10


def main():

    print("The program is provided two strings by the user. The first is the string proper. The second is the substring\n" +
    "which will be searched for in the first string. The second occurrence of the substring will have the index returned and\n" +
    "printed to the console. If there is only one (or zero) instances of the substring in the string, it will return -1.")

    orig_strng = input("\nPlease input a string to search through for a specified substring: ") # prompt user for string and assign result to variable
    sub_strng = input("Please enter the substring you are searching for: ") # prompt user for substring and assign to variable 

    #orig_strng = "Mississippi"
    #sub_strng = "ss"

    second_occurrence_i = matt_find(orig_strng, sub_strng) # call matt_find with original string and substring as arguments. Assign returned result to variable
    print() # empty print for space between explanation and print
    print(second_occurrence_i) # print returned index
    
    if second_occurrence_i > -1: # significant print statement depending on whether the second instance of the substring was found in the string or not
        print(f"The second instance of the substring in the original string begins at index: {second_occurrence_i}")
    else:
        print(f"There was either 0 or only 1 occurrence of the substring in the string. Thus {second_occurrence_i} was returned.")
        

def matt_find(original_string, ss):
    i = 0 # index for ss
    j = 0 # index for original_string
    occurrence_counter = 0 # track the instance number of how many times the substring has appeared in the string
    j_counter = 0 # track how many indices j has moved since the match of the first index of the substring
    scnd_inst_frst_i = 0 # second instance, first index variable. Will be returned to calling function if found, else -1 returned
    orig_len = len(original_string) # length of original string assigned to variable
    SECOND_INST = 2

    ss_len = len(ss) # the length of ss is assigned to subscript length (ss_len)

    while j < orig_len: # E.g. Mississippi (so 11)

        if ss[i] == original_string[j]: # if value at index i of ss is equal to value at index j of original_string
            if i == ss_len - 1: # if i, which is the index of the substring, is equal to ss_len - 1, which is the last index of the substring
                occurrence_counter += 1 # add one to occurrence/instance tracker when the value in the substring index (i) matches the value in the string index (j)
                i = 0 # reset i to 0 so that we can start from the index 0/first element again in order to look for the second occurrence of a substring

            if occurrence_counter == SECOND_INST: # if the occurrence counter is 2, it means we have found the second occurence of the substring in the string. Could change the constant to a variable and receive it as a parameter
                scnd_inst_frst_i = j - j_counter # assign the second instance's first index variable equal to j (used for indexing the original string) minus j_counter (which tracks how 
                # many times j has been incremented since matching the first index of the substring) to get the first index of the second instance of the matched substring in the original string
                return scnd_inst_frst_i # return index number to the calling method

            #if i >= 0 and occurrence_counter > 0:
            i += 1 # increment i by 1
            j_counter += 1 # track the number of increments since first match between substring[0] and originalstring[j]
                
        elif ss[i] != original_string[j] and i > 0: # else if value at index i of ss is not equal to value at index j of original_string and i is greater than 0
            i = 0 # reset i to 0 since you have to start with the first index of substring again. Failure to reset this to 0 could lead to a premature occurrence_counter increase, which would cause a incorrect/ 
            # premature index to be returned to calling method
            j_counter = 0 # reset to 0 or you will be tracking the number of indices away from the first match of substring[0] to originalstring[j]

        if j < orig_len: # if j is less than the length of the original string
            j += 1 # increment j by 1

    return -1 # If 0 matches or only 1 match is found, return -1. 
            
main()   

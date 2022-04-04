# File:    Assgn9forbes.py 
# Project: CSIS2101 Assignment 9
# Author:  Matthew Forbes 
# History: Version 1.1 March 21, 2022


'''
1. In Python operation on strings when you use replace(oldstring, newstring) function all the old strings are replaced by the new string. 
But write your own Replace function which replaces just the second instance of the old string with the new string. In this problem you
dont want to replace all old strings with a new string. But just the second instance of that string. Name the python function that does it
as FirstNameFirstAlphabet LastNameLastAlphabet(UpperCase)Replace. This should take three arguments. The original string, substring to be 
replaced and the new substring used to replace with. 

2. Many companies use telephone numbers like 555-GET-FOOD so the number is easier for their customers to remember. On a particular dial pad 
the alphabetic letters are mapped to numbers in the following fashion:

A D and G - 9
B E and H - 8
C F and  I - 7
J M and P - 6
K N and Q - 5
L O R and S - 4 
T W and Z - 3
U and X - 2
V and Y - 1

Write a program that asks the user to enter a 10 character telephone number in the format XXX-XXX-XXXX or a 7 character telephone number in 
the format XXX XXXX (In both formats with or without the hyphen “-“). You don't have to validate the format. It can be all alphabets or mixture
of alphabet and Numbers. The application should display the telephone number with any alphabetic character that appeared in the original 
translated into their numeric equivalent. 

The program should handle upper case and lower case alphabets. The phone number can contain hyphens ( - ) like in the first example or spaces 
like in the second example. Name the python function that does it  as FirstNameFirstAlphabet LastNameLastAlphabet(UpperCase) NumberConverter 
and this function needs to be called from main. 


3. Write a program that accepts a sentence as an input and converts each word to pig latin. In this version to covert a word into pig latin, 
you reverse the sentence word by word and for each word you replace the vowels with a respective number. 9 for A, 3 for E, 1 for I, 0 for O 
and 6 for U respectively. The program should handle only upper case alphabets and can assume there are no special characters like (.) or (') 
or (-) in the sentence. Name the python function that does it  as FirstNameFirstAlphabet LastNameLastAlphabet(UpperCase) PigLatin and this 
function needs to be called from main. 

'''



def main():

# 1.

    # Input

    print("The program is provided three strings by the user. The first is the string proper. The second is the old substring to have the\n"
    "be replaced, which will be searched for in the first string. The third string is the substring you would like to replace the old\n"
    "substring with. The second occurrence of the old substring (if it exists) will be replaced with the new substring in the first string,\n"
    "and the resulting new string (the now altered first string) will be returned and printed to the console. If there is only one (or zero)\n"
    "instances of the old substring in the first string, the program will return the original string unaltered.")

    orig = input("\nPlease enter a string: ") # prompt user for string and assign result to variable
    sub = input("Please enter the substring that you would like to replace the second instance of: ") # prompt user for substring and assign to variable 
    replacement = input("Please enter what you would like to replace the old substring with: ") # prompt user for replacement substring and assign to variable

    #orig = "Mississippi"
    #sub = "ss"
    #replacement = "zz"

    new_string = mSReplace(orig, sub, replacement) # Call mSReplace and pass in variables as arguments in respective order. Assign returned result to new_string variable

    # Output
    if new_string != orig: # if new_string is not equal to original string
        print(f"\nThe new string after the replacement is: {new_string}\n")
    else: 
        print(f"\nThe substring to be replaced occurs less than twice in the original string, so the original string \"{orig}\" has been returned unaltered.\n")
        


# 2.
    # Ouput
    original_phone_num, translated_phone_num = mSNumberConverter() # assign returned results to respective variables
    print(f"\nThe original phone number \"{original_phone_num}\" translated to only numbers is: {translated_phone_num}\n") # print the phone_num to console in significant print statement


# 3. 
    intitial_sentence, pig_latin_sentence = mSPigLatin()
    # Output
    print(f"\nThe original sentence, \"{intitial_sentence}\", in pig latin is: {pig_latin_sentence}")



#1. 
# Processing
def mSReplace(original_string, old_substring, replacement_strng):
    
    first_i = original_string.find(old_substring) # get the first index of the first instance of the old substring in the original string and assigns to first_i
    if first_i == -1: # if find() returns -1, no instances of the provided substring were found, so return the original string
        return original_string # 

    newString = original_string[first_i + len(old_substring):] # String slicing from the first index of the first instance of the substring plus the length of the old substring
    # to be replaced. This puts index 0 of the new string exactly 1 element after the last element of the first instance of the substring in the original string. E.g. Mississippi
    # (as the original string) and ss (as the old substring to be replaced) would be 2 + 2 = 4, which means the resulting newString would start at index 4 of the original string,
    # and would thus be set to "issippi".


    if newString.find(old_substring) == -1: # use find() again to search for the next occurrence of the old substring to be replaced. If find returns -1, no instances were found, so
        # return the original string
        return original_string 

    else: # else (if find() does not return -1)
        first_i += len(old_substring) + newString.find(old_substring) # In the Mississippi example: first index (2) + the length of the old substring (2) + the new string's index of the first 
        # occurrence of the substring (1) is assigned to first index (5)
        last_i = first_i + len(old_substring) # The first index (5) + the length of the old substring (2) = 7

        first_part = original_string[:first_i] # String slice the first part of the original string we want to keep, starting at index 0, with the index that the second instance of the old substring starts at as our limit
        last_part = original_string[last_i:] # String slice the last part of the original string we want to keep, starting with the last index of the second instance of the old substring in the original, and ending at the last
        # index of the original string (inclusive) 

        final_string = first_part + replacement_strng + last_part # The final string is created via concatenation: The first part + the replacement string + the last part

        return final_string # return the final string or signicant print statement to calling function



# 2.
def mSNumberConverter():

    # Input
    phone_num = input("Please enter a 10 character telephone number in the format \"XXX-XXX-XXXX\" or a 7 character telephone number in the format \"XXX XXXX\" \n"
    "(In both formats with or without the hyphen \"-\"). The number must contain either hyphens or spaces like in the first or second example: ")

    # Processing
    original_num = phone_num

    #phone_num = "555-GET-FOOD"

    phone_num = phone_num.upper() # change to uppercase to handle both lower and uppercase more easily
    
    i = 0 # phone number index
    replace_num = "" # variable to hold the number that will be replaced
    first_half = "" # variable that will have the first half of the number assigned to it
    second_half = "" # variable that will have the last half of the number assigned to it

    while i < len(phone_num): # while i is less than the length of the phone number
        if phone_num[i].isdigit() or phone_num[i].isspace() or phone_num[i] == "-": # if the value at the index is a digit, space or dash, increment i by 1
            i += 1

        elif phone_num[i].isupper(): # else if the value at the index is an uppercase letter:
            first_half = phone_num[:i] # string slice the phone number string, from index 0 to index i is assigned to the first half variable
            second_half = phone_num[i+1:] # string slice the phone number string, from index i+1 to the last index is assigned to the second half variable. Starting the
            # slice at i+1 means that there is a one character space between the first_half and last_half when concatenated. This space is where the replacement character
            # will go.
            

            if phone_num[i] == "A" or phone_num[i] == "D" or phone_num[i] == "G": # if the value at index i of phone_num is equal to "A", "D", or "G": assign "9" to replace_num
                replace_num = "9"
            elif phone_num[i] == "B" or phone_num[i] == "E" or phone_num[i] == "H":
                replace_num = "8"
            elif phone_num[i] == "C" or phone_num[i] == "F" or phone_num[i] == "I":
                replace_num = "7"
            elif phone_num[i] == "J" or phone_num[i] == "M" or phone_num[i] == "P":
                replace_num = "6"
            elif phone_num[i] == "K" or phone_num[i] == "N" or phone_num[i] == "Q":
                replace_num = "5"
            elif phone_num[i] == "L" or phone_num[i] == "O" or phone_num[i] == "R" or phone_num[i] == "S":
                replace_num = "4"
            elif phone_num[i] == "T" or phone_num[i] == "W" or phone_num[i] == "Z":
                replace_num = "3"
            elif phone_num[i] == "U" or phone_num[i] == "X":
                replace_num = "2"
            elif phone_num[i] == "V" or phone_num[i] == "Y":
                replace_num = "1"
        
            phone_num = first_half + replace_num + second_half # concatenate the first_half string slice of the phone_num string with the replace_num string, and the second_half
            # string in that order and reassign result to phone_num. The replace_num is concatenated at index i, so as i is incremented, the phone_num is progressively checked for any letters
            # to translate into numbers one index at a time.

            i += 1 # Increment i by 1 to advance to next index (which in this case is the next character).

        else: # else (if) value at index i of phone_num is not a digit, space, dash or an uppercase letter, indicate invalid character entered and ask the user to try again
            phone_num = input("Error. Invalid character entered. Please try again using only alphanumerics, spaces, and dashes \"-\": ")
            phone_num = phone_num.upper() # return newly input string in uppercase again
            i = 0 # reset i to zero to restart the translation process at the first index (and therefore the first character in the phone_num string)

    return original_num, phone_num


# 3. 
def mSPigLatin():

    # Input
    init_sentence = input("Please input a sentence to convert each word to pig latin: ")

    # Processing
    initial_sentence = init_sentence.upper() # return uppercase of string and assign to variable
    word_list = initial_sentence.split() # Split string up into separate words by using standard space as delimiter. Puts words into list as individual elements, so they are now mutable
    word_list.reverse() # reverse list elements (words)

    letter = 0 # set letter equal to 0 (use as index in the inner list)
    ss_word_list = [] # initialize substring word list to empty
    final_list = [] # initialize final list to empty

    for word in word_list: # for each word in the word list
        while letter < len(word): # while letter (index) is less than the length of the word in the word_list

            if word[letter] == "A": # if the value at the index of word is equal to "A", insert "9" into the index "letter" of the substring word list. Since this is if, elif, else, 
                # the program will compare the value at the index to the specified string (letter) and then increment letter by 1 to go to the next index (letter in this case)
                ss_word_list.insert(letter, "9")
            elif word[letter] == "E":
                ss_word_list.insert(letter, "3")
            elif word[letter] == "I":
                ss_word_list.insert(letter, "1")
            elif word[letter] == "O": 
                ss_word_list.insert(letter, "0")
            elif word[letter] == "U":
                ss_word_list.insert(letter, "6")
            else:
                ss_word_list.insert(letter, word[letter]) # if the value at index "letter" of word does not equal any of the specified strings above, the value at the index "letter" of word is inserted into the 
                # substring word list at the "letter" index

            letter += 1
        
        final_list.append(ss_word_list) # when one element (or "word") in the list has been looped through fully by the while loop, the substring word list is appended to the final_list before the substring word
        ss_word_list = [] # list is reset to empty for the iteration through the next element (word) in the word_list
        letter = 0 # letter is reassigned to 0 in order to begin at index 0 (and thus the first "letter") of the next "word"

    # Once the for loop is complete, final_list is a nested list with each word of the original sentence as an inner list, with the character replacements having been made, and the words in reverse order as required.
    # Now there is just the need to turn it back into a string

    new_sentence = "" # initialize new_sentence to empty
    new_word = "" # initialize to empty
    
    #print(final_list)

    for word in final_list: # for each word in the final list
        new_word = "" # reassign new word to empty after each word has completed it's iteration in the inner for loop
        for char in word: # for each character in word (this iterates through the characters of the "words" that are the inner lists of final list)
            new_word += char # concatenate the new_word string (which is empty initially) and the current letter (which can be done because the letter is a string)
        new_sentence += new_word + " " # Once a word has been iterated through, concatenate the resulting "new_word" and a space (" ") to the new_sentence variable. 
        # control returns to first line of outer for loop which resets the new_word to empty. Without resetting new_word to empty, you will continually concatenate 
        # # onto it with one less word added with each iteration of the final_list (outer loop)

    return init_sentence, new_sentence # return to calling function for variable to "catch" for significant print statement


            
main()
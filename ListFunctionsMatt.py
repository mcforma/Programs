# File:    LoopsForbes.py 
# Project: CSIS2101 Assignment 8
# Author:  Matthew Forbes 
# History: Version 1.1 March 14, 2022

'''
The point of this program is to create various list functions as described below:

•	def range_of_list_firstname( number_list ): 
# returns range of the list. Range is largest number in the list - the smallest number in the list. You can use already available functions max and min on a list. So if the largest 
# number is 13 and smallest number in the list is 5, then return 8 (which is 13 - 5). 

•	def sum_of_list_firstname( number_list ):
In this function write your own function by using  a for loop to find the sum of the numbers in the list. Once you find the sum using your method check whether the sum you found is 
equal to the builtin function sum in a list. 
#returns two arguments 1)the sum of the numbers in the list and 2) also a true or false based on the sum you calculated is same as the sum calculated using the builtin function. So 
# this function has to return two values - the sum and a Boolean variable. 

•	def mean_of_list_firstname( number_list ):
#returns mean or average. Use the sum_of_list (..) function(previous fn) to calculate the average. Mean is the sum/number of elements in the list. 

•	def head_tail_list_firstname( number_list ):
#returns the difference between the head and tail of the list. Head is the first element in the list and tail is the last element in the list.  Find the difference between the head 
# value and the tail value and return the value. So if first value is 9 and the last value in the list is 12, this function returns -3 which is 9 - 12. 

•	def median_of_list_firstname( number_list_copy ):
#returns median of the list. Here a deep copy of the number_list using list comprehensions is sent as an argument. Median is the middle number of the list after the list is sorted 
# in ascending order. If numbers are even, median is the average of the two middle numbers. 
So for example if the list has 11 numbers, median is the 6th element or index = 5 and if the list has 10 elements median is the average of the 5th element and 6th element 
( index = 4 and index = 5) You can use the available function sort to sort the numbers. 

•	def clip_the_list_firstname( number_list, clip_num ):
#This function takes two arguments the original number_list and the clip_num which is an integer
# returns the clipped array based on the clip_num. Clipping an array is replacing all the numbers greater than the number provided to that number. So for example if the list is [3,17,5,9,1,11]
#  and the clip_num is 8, returned array is [3,8,5,8,1,8]. So all numbers greater than the clip_num (here 8) is replaced by the clip_num(which is 8 in this example). Clip_num that takes a 
# maximum value as an argument and changes any value in the list that is higher than the specified maximum value to be the same as the maximum value. This function could also be called “haircut”,
#  in that it takes values that are too high, and cuts them down to the maximum allowable height. (Think of a scissor going through your hair and trimming the ones that are too long.)

•	Within your main function (name your main as firstnameList) create an empty list ask for the number of items in the list n and using a loop append the n numbers input by the user to the list.
  The program should then call each of the functions provided above by passing in the list you created as an argument and test your functions. 

•	Except for the median, where you make a deep copy of the list using List comprehensions and pass the copy of the list and not the original list.  And then display the return values within 
this firstNameList() with meaningful messages as shown below:

Given List:  		#prints the list here
Range of the List is: 	#gives the range value of the list
Sum of the List is: 	#displays the sum of the list calculated using the sum_list
Sum of the List found using sum_list is same as the sum found using the sum function: ____ 
#( This should be a True or False and indicates whether your function and builtin function gives the same answer )
Mean of the List is: 	#gives the mean of the list
Median of the List is:		#gives the median of the list. 
Clipped List clipped on the number __ is:		#gives the clipped list. 
(You can hard code the clipNum or ask it to be provided as a user input)

Don't hard code the length of the list. It should work for any list including an empty list where n = 0. 

All functions should be in one file named ListFunctionsFirstname.py with your first name substituted and please submit as a zip file. 


'''

import sys

def mattList():

    number_list = [] # Create empty list
    n = 0 # initialize to 0 for while loop to enter

    while n <= 0: 
        if n < 0:
            print("n cannot be less than 0, please try again.")
        n = int(input("How many items are in the list: ")) # Ask for number of items in the list and assign to n
        if n == 0: # When Brandon asked you in class, you said that if the user enters 0, to just put 0's all the way down the display. Math cannot
            # be performed on empty numbers, so I handle it here on the front end instead of multiple times down below because it's more efficient
            print("\nGiven List:\t 0")
            print("Range of the List is:\t 0")
            print("Sum of the List is:\t 0") 
            print("Sum of the List found using sum_list is the same as the sum found using sum function: False") # Empty bool is set to False
            print("Mean of List is:\t 0")
            print("The difference between the Head and Tail of the List is:\t 0")
            print("Median of the List is:\t 0")
            print("Clipped List clipped on the number 0 is: []")
            print("Exiting....")
            sys.exit()
            




    # if we wanted to force the user to enter at least 1:
    '''while n < 1: # will enter at least once since 0 is assigned to n. Will loop until user enters 1 or greater
        n = int(input("How many items are in the list: ")) # Ask for number of items in the list and assign to n
        if n < 1:
            print("n cannot be less than 1, please try again.") 
    '''



    counter = 1 # Start counter at 1 for f string below inside while loop. Could also use 0 and then {counter+1} for the f string

    print("Please enter the numbers one at a time, following each number with the enter key.")
    while counter <= n: # Since the counter is not 0 based, but starting at 1, use <= instead of < to get the correct number of items in list as dictated by n

        number_list.append(int(input(f"Element {counter}: "))) # Prompt user to input element m number
        counter += 1 # increment counter by 1 towards n.

    print(f"\nGiven List:\t {number_list}") #print the given list
    
    num_range = range_of_list_matt(number_list) # Call the range_list function with the newly created list, number_list, as the argument and assign to num_range variable
    print(f"Range of the List is:\t {num_range}") # print the range

    sum_total, sums_areEqual = sum_of_list_matt(number_list) # Call the sum_list function with the number_list as a parameter. Assign returned results to sum_total 
    # (sum of list) and sums_areEqual (is the sum of list function equal to the sum() result?)
    print(f"Sum of the List is:\t {sum_total}") # print significant list with the sum of the list function
    print(f"Sum of the List found using sum_list is the same as the sum found using sum function:\t {sums_areEqual}") 
    # print True if sum_list function result is equal to sum function, or False if not equal

    mean_list = mean_of_list_matt(number_list) # Call mean_list with number_list as argument and assign returned result to mean_list variable
    print(f"Mean of List is:\t {mean_list}") # significant print statement with mean_list


    head_tails_num = head_tail_list_matt(number_list) # Call head_tail_list function with number_list as argument and assign result to variable
    print(f"The difference between the Head and Tail of the List is:\t {head_tails_num}")


    number_list_copy = [item for item in number_list] # deep copy list item for item
    median_num = median_of_list_matt(number_list_copy) # Call median_list function with the deep copy of list as argument. Assign returned result to variable
    print(f"Median of the List is:\t {median_num}")
    

    clip_num = int(input("Please enter the integer to \"clip\" with: "))
    clipped_array = clip_the_list_matt(number_list, clip_num)
    print(f"Clipped List clipped on the number {clip_num} is: {clipped_array}")




def range_of_list_matt(number_list): # Define range_list function with number_list as parameter
    num_range = max(number_list) - min(number_list) # maximum number in number_list - minimum number is assigned to num_range
    return num_range # return result to calling method (matt_list)


def sum_of_list_matt(number_list): # sum_list function

    sum_num = 0 # assign 0 to sum tracker
    for num in number_list: # for number in number_list, add each number to the sum_num variable each iteration
        sum_num += num

    sums_equal = None # sums_equals is initialized to None so that the scope extends beyond the if/else 
    if sum_num == sum(number_list): # if the sum_num (variable containing result of sum_list) is equal to sum function of the list
        sums_equal = True # set sums_equal to True
    else:
        sums_equal = False # else if not true, set sums_equal to False
    
    return sum_num, sums_equal # Return the sum_num and sums_equal to calling method where it will be caught by respective variables there
        

def mean_of_list_matt(number_list): # mean_list function
    total, sums_areEqual = sum_of_list_matt(number_list) # use sum_list function to sum the list by providing list as argument and assigning result to total
    num_of_nums_in_list = len(number_list) # return number of items in list and assign to variable

    mean_list = total / num_of_nums_in_list # mean (mean_list) = sum (total) / number of elements in list (num_of_nums_in_list)
    return mean_list # return to calling function


def head_tail_list_matt(number_list): # head_tail function finds difference between first and last element
    head_tail_value = number_list[0] - number_list[-1] # index 0 == first element. index -1 is the last index (length -1), which == last element. 
    # Subtract last element from first, assign result to variable
    return head_tail_value



def median_of_list_matt(number_list_copy): # median_list method
    number_list_copy.sort()

    list_len = len(number_list_copy)
    
    median_index = -1 # 
    median1_index = 0 # "first median" number's index when the list length is even
    median2_index = 0 # "second median" number's index when the list length is even. median1 and median 2 will be summed and averaged for medium in case of even length list
    median = 0

    if list_len % 2 == 1: # if list_len divided by 2 has a remainder of 1, it is odd, meaning the middle element is the median (assuming list is sorted in ascending order)
        median_index = list_len // 2 # index is 0 based. List length integer divided by 2 will provide the index of the middle element.
        # For example, if there are 15 elements (items) in a list, the length is 15, but the indices are 0 through 14 (15 is out of bounds). So you integer divide the length (15)
        # by 2, and you get 7 because the remainder is dropped, only the integer is kept. 7 is the number of the middle index (index 7) in a list that goes up to index 14, since 
        # indices are 0 based. 
        median = number_list_copy[median_index] # Assign number at the median index of the list to the median variable
        return median # Return median to catching variable in calling function.

    else:
        median1_index = list_len // 2 - 1 # to get the "first median" number's index, take the length (e.g. 14) integer divide by 2 (= 7) and then subtract 1 (6). 
        median2_index = list_len // 2 # # to get the "second median" number's index, take the length (e.g. 14) integer divide by 2 (= 7). 6 ("first" median number's index)
        # and 7 ("second median" number's index) are both 7 away from the head (0) and tail (13) indices respectively
        median = (number_list_copy[median1_index] + number_list_copy[median2_index]) / 2 # sum the two numbers at the "first" and "second" median indices and divide by 2 to get the median 
        # for an even length list. Return median to calling function and assign to catching variable
        return median
    


    # Can also solve with for loop. Increment i by 1 and decrement j by 1 each iteration so that they are approaching one another
    '''i = int(0)  # first index counter. Start at 0 for first index of list
    j = list_len - 1 # second index counter. Start at list length - 1 to get last index, regardless of list length
    for num in number_list_copy:  # enter for loop to loop through all nums in the number list copy
        if i == j : # if i (first index counter) is equal to j (second index counter), the median's index will be equal to both i and j since there are an odd number of elements
            # with an odd number of elements, the index counters will be 2 away from one another and then will be the same number
            median = number_list_copy[i] # assign the number from the number list that has the index i to the median. Could also use j instead of i
            return median

        if j - i == 1: # with an even number of elements, the index counters will be right next to one another (difference of 1) when the two middle indices are selected
            median = (number_list_copy[j] + number_list_copy[i]) / 2 # Add the numbers in the respective indices together and divide by 2 to average
            return median # return result to calling function to be caught by variable
        i += 1 # increment i by 1 and decrement j by 1 before testing again. This will ensure there is always a 2 number swing towards each other (because i increases by 1 and j decreases by 1)
        j -= 1 # until either they are the same number, or j is 1 number greater than i. In case of the latter, those are the two middle numbers.
    '''
    
            
def clip_the_list_matt(number_list, clip_num):
    counter = 0 # create index counter
    while counter < len(number_list): # loop while the counter index is less than the length of the number_list
        if number_list[counter] > clip_num: # if the value in index counter is greater than the clip_num
            number_list[counter] = clip_num # reassign the clip_num to said index
        counter += 1 # increment counter by 1 to proceed through the list
    return number_list # return the clipped_list


mattList()





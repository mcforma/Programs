# Find average score of a gymnast.

import sys

def main():
    '''
    The scores are [9.3, 9.9, 2.2, 8.4, 5.6, 7.8]
    Remove largest value (9.9) and smallest which is 2.2
    Then find the average of the remaining scores (9.3, 8.4, 5.6, 7.8)
    '''

    print("The scores from the judges are entered and then averaged after removing\n"
    "the highest and lowest scores. Any score that is not within the valid range\n"
    "(0 through 10) will result in additional scores longer being accepted and the\n"
    "score being averaged. Likewise, once all the scores have been entered, enter a\n"
    "number outside of the valid range (e.g. -1 or 11) to begin the averaging process.\n")

    list_scores = [] # Create empty list to  insert scores from user into
    i = 0   # Variable to track index
    score = 0 # declare and initiate score variable at 0; any number between 0 and 10 (inclusive) will do.

    while score >= 0.0 and score <= 10.0: # Ensure that an unknown number of scores will be able to be added as long as valid scores are entered.
        # The while loop will always enter at least once since score was initially initialized with a value of 0
        score = int(input("Please enter the gymnast's score between 0 and 10: ")) # Get score from user
        if score >= 0.0 and score <= 10.0: # if the provided score is in the valid range, add it to the list with an insertion. If not, do not add, and while loop will end
            list_scores.append(score)
            i += 1

        else:
            print("\nAn invalid score has been provided. No further scores may be entered and the average score will now be processed with the provided valid scores.")
    print(list_scores)
    if len(list_scores) > 2:
        # Alert user that the highest and lowest scores have each been removed and show what each is.
        print(f"The highest ({max(list_scores)}) and lowest ({min(list_scores)}) score have each been removed to reduce the chance of bias.\n") 
        list_scores.remove(max(list_scores)) # Remove highest score from list
        list_scores.remove(min(list_scores)) # Remove lowest score from list

        average, num_scores = calc_avg_score(list_scores) # Call calc_avg_score function with list_scores as parameter and assign returned results to average and num_score respectively. 
        print(f"The average score of the gymnast, excluding the discarded highest and lowest scores, is {average:.1f}, based upon {num_scores} submitted scores.") # Meaningful print statement with average result rounded to nearest .1 and total scores provided.
    
    elif len(list_scores) == 1:
        print(f"Only one valid score was provided. The score was {list_scores[0]}.")
        print("Goodbye.")
        sys.exit()

    else:
        print("No valid scores have been provided. Goodbye.")
        sys.exit()


def calc_avg_score(ls):
    # To find the average score of the scores in the list ls which is
    # The scores put by different judges (unknown number of scores)
    # Remove smallest score and largest scores to avoid bias
    # Find average of remaining scores

    length = len(ls) # Assign length of list to a variable

    total = 0 # Assign total counter to 0
    for score in ls: # for loop to iterate through all numbers in the list.
        total += score # Add each score to total

    average = total / length # Calculate average
    return average, length # Return the average and length of the list (which is the number of valid scores, excluding the discarded scores)


main()
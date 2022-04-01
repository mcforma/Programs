# gradeavg_while.py
# Week 4 participation question is rewrite the gradeavg.py program using a while loop.
# Calculate average grade of n students where each students grade is entered.

def gr_avg():
    n = int(input("Please enter the number of students: "))

    counter = 1
    sum_grades = 0

    while counter < n+1:
        grade_score = int(input("Enter the student's grade: "))
        sum_grades += grade_score
        counter += 1

    print(f"Total grades is: {sum_grades}")
    if n != 0:
        average = sum_grades/n
        print(f"Average of {n} students is: {average}")
    else:
        print("There are no students")
gr_avg()


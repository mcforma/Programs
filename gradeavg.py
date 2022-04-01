# gradeavg.py

def gr_avg():
    n = int(input("Please enter the number of students: "))

    sum_grades = 0

    for score in range(1, n+1):
        grade_score = int(input("Enter the student's grade: "))
        sum_grades += grade_score

    print(f"Total grades is: {sum_grades}")
    if n != 0:
        average = sum_grades/n
        print(f"Average of {n} students is: {average}")
    else:
        print("There are no students")
gr_avg()

# Week 4 participation question is rewrite the above program using a while loop.
# Calculate average grade of n students where each students grade is entered.
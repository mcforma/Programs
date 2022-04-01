# grade_avg_sentinel
# We are calculating the average grade of students when we don't know how how many students
# We use a sentinel value of -1 which cannot be a valid score

def gr_avg():
    grade_score = int(input("Enter the student's grade: "))
    counter = 0
    sum_grades = 0

    while grade_score != -1:
        counter += 1
        sum_grades += grade_score
        grade_score = int(input("Enter the student's grade: ")) 

    if counter == 0:
        print("There are no grades to calculate")
    else:
        average = sum_grades/counter
        print(f"Average of {counter} students is: {average:.2f}")

gr_avg()


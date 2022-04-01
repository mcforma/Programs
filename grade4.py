# grade3.py
# Calculating the letter grade from the point grade with the "and" logical operator.

'''
If gradepoint greater than or equal to 90 its an A
If gradepoint greater than or equal to 80 its an B
If gradepoint greater than or equal to 70 its an C
If gradepoint greater than or equal to 60 its an D
Otherwise F
If grade is less than 0 or greater than 100 print invalid grade
'''

def main():
    grade_point = float(input("Please enter the point grade of the student: "))

    if grade_point < 0 or grade_point > 100:
        print("Invalid grade point.")
    if grade_point >= 90 and grade_point <= 100:
        grade_ltr = "A"
    elif grade_point >= 80 and grade_point < 90:
        grade_ltr = "B"
    elif grade_point >= 70 and grade_point < 80:
        grade_ltr = "C"
    elif grade_point >= 60 and grade_point < 70:
        grade_ltr = "D"
    else:
        grade_ltr = "F"

    print(f"The grade for {grade_point} is {grade_ltr}")

main()
        
    
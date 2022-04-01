#gradeavg.py

def gr_avg():
    n = int( input( "Please enter the number of students: " ) )

    sum_grades = 0

    for score in range( 1, n + 1 ):
        grade_score = int( input ( "Enter the grade of the student: " ))
        sum_grades += grade_score

    print("Total grades is: ", sum_grades)
    if n != 0:
        average = sum_grades/ n
        print( "Average of ", n, "students is: ", average)
    else:
        print("There are no students or n == 0")
        
gr_avg()
'''
Week 4 participation question is rewrite the above program using a while loop.
Calculate average grade of n students where each students grade is entered
'''

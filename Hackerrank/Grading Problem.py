# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        grades[i] = do_round(grades[i])
    return grades

def do_round(grade):
    if grade < 38:
        return grade
    dis_from_next_multiple = 5 - grade % 5
    if dis_from_next_multiple >= 3:
        return grade
    else:
        return grade + dis_from_next_multiple
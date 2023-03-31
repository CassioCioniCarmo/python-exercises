"""
    Exercice - 3: Finding the percentage
    The provided code stub will read in a dictionary containing key/value pairs of name:[marks] 
    for a list of students. Print the average of the marks array for the student name provided, 
    showing 2 places after the decimal.
    
    Sample Input 0:
    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika
    
    Sample Output 0:
    56.00
    From HackerRank
    
    Cassio Cioni Carmo - 03/30/2023
"""

if __name__ == '__main__':
    number_students = int(input())
    student_marks = {}
    for _ in range(number_students):
        name_students, *line = input().split()
        scores_students = list(map(float, line))
        student_marks[name_students] = scores_students
    query_name = input()
    
    sum_marks = 0
    for i in range(len(student_marks[query_name])):
        sum_marks = sum_marks + student_marks[query_name][i]
            
    print(("{:.2f}".format(((sum_marks)/len(student_marks[query_name])))))

"""
    Exercise - 5: Nested Lists
    Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s)
    of any student(s) having the second lowest grade.
    
    Sample Input 0
    5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39
    
    Sample Output 0:
    Berry
    Harry
    
    Cassio Cioni Carmo - 04/01/2023
"""

if __name__ == '__main__':
    dic_name = {}
    for _ in range(int(input("Number of students:"))):
        student_name = input("Students names:")
        student_score = float(input("Students score:"))
        dic_name[student_name] = student_score
        
    dic_name_ordered = sorted(dic_name.items(), key = lambda x: x[1])
    last_student = dic_name_ordered[0]
        
    
    for i in range(len(dic_name_ordered)):
        if last_student[1] != dic_name_ordered[i][1]:
            penultimate_student = dic_name_ordered[i][1]
            break
        
    list_second = []
    for i in range(len(dic_name_ordered)):
        if penultimate_student == dic_name_ordered[i][1]:
            list_second.append(dic_name_ordered[i][0])
            
    sorted_list_second = (sorted(list_second))
    for i in range(len(sorted_list_second)):
        print(sorted_list_second[i])

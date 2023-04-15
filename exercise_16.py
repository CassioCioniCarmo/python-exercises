"""
    Exercise - 16:  String Validators

   Sample Input
    qA2

    Sample Output
    True
    True
    True
    True
    True
        
    Cassio Cioni Carmo - 04/15/2023
"""
if __name__ == '__main__':
    string_input = input()
    flag = False
    
    for char in string_input:
        if char.isalnum():
            flag = True
            break
        else:
            flag = False
    if flag:
        print("True")
    else:
        print("False")      
            
    for char in string_input:
        if char.isalpha():
            flag = True
            break
        else:
            flag = False
    if flag:
        print("True")
    else:
        print("False")   
            
    for char in string_input:
        if char.isdigit():
            flag = True
            break
        else:
            flag = False
    if flag:
        print("True")
    else:
        print("False")   
        
    for char in string_input:
        if char.islower():
            flag = True
            break
        else:
            flag = False
    if flag:
        print("True")
    else:
        print("False")   
    
    for char in string_input:
        if char.isupper():
            flag = True
            break
        else:
            flag = False
    if flag:
        print("True")
    else:
        print("False")   

"""
   Exercise - 9:  Lists

   Sample Input 0
    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

    Sample Output 0
    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
    
    Cassio Cioni Carmo - 04/07/2023
"""

import re
if __name__ == '__main__':
    N = int(input())
    
    number_list = []
    
    for i in range(N):
        command = input()
        if "insert" in command:
            number_position_value = re.findall(r'\d+', command)
            number_list.insert(int(number_position_value[0]), int(number_position_value[1]))
        if "print" in command:
            print(number_list)
        if "remove" in command:
            number_position_value = re.findall(r'\d+', command)
            number_list.remove(int(number_position_value[0]))
        if "append" in command:
            number_position_value = re.findall(r'\d+', command)
            number_list.append(int(number_position_value[0]))
        if "sort" in command:
            number_list.sort()
        if "pop" in command:
            number_list.pop(-1)
        if "reverse" in command:
            number_list.reverse()

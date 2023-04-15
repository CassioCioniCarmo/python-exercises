"""
    Exercise - 15:  Find a string

   Sample Input
    ABCDCDC
    CDC

    Sample Output
    2
        
    Cassio Cioni Carmo - 04/15/2023
"""
def count_substring(string, sub_string):
    total_sub_string = 0
    for i in range(len(string)):
        if string[i: i +len(sub_string)] == sub_string:
            total_sub_string += 1
    
    return total_sub_string

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
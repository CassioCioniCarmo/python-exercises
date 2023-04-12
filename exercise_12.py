"""
    Exercise - 12:  String Split and Join

    Sample Input
    this is a string   

    Sample Output
    this-is-a-string
        
    Cassio Cioni Carmo - 04/12/2023
"""

def split_and_join(line):
    splite_string = line.split(" ")
    joining_string = "-".join(splite_string)
    return joining_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
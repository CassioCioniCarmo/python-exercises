"""
    Exercise - 18:  Text Wrap

    Sample Input 0
    ABCDEFGHIJKLIMNOQRSTUVWXYZ
    4

    Sample Output 0
    ABCD
    EFGH
    IJKL
    IMNO
    QRST
    UVWX
    YZ
        
    Cassio Cioni Carmo - 04/16/2023
"""
import textwrap

def wrap(string, max_width):
    new_string = textwrap.fill(string, max_width)
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
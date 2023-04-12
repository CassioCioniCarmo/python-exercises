"""
    Exercise - 11:  sWAP cASE
    You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

    Sample Input 0
    HackerRank.com presents "Pythonist 2".

    Sample Output 0
    hACKERrANK.COM PRESENTS "pYTHONIST 2".
        
    Cassio Cioni Carmo - 04/11/2023
"""

def swap_case(string_input):
    string_swap = string_input.swapcase()

    return string_swap

if __name__ == '__main__':
    string_input = input()
    result = swap_case(string_input)
    print(result)
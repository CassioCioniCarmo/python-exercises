"""
   Exercise - 10:  Tuples
   Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. 
   Then compute and print the result of hash(t).

   Sample Input 0

    2
    1 2
    Sample Output 0

    3713081631934410656
        
    Cassio Cioni Carmo - 04/09/2023
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_number = tuple(integer_list)
    print(hash(tuple_number))

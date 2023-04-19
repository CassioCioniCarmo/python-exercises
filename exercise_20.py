"""
    Exercise - 20:  Exceptions!

    Sample Input
    3
    1 0
    2 $
    3 1

    Sample Output
    Error Code: integer division or modulo by zero
    Error Code: invalid literal for int() with base 10: '$'
    3
        
    Cassio Cioni Carmo - 04/18/2023
"""
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        try:
            a,b = map(int, input().split())
            print(int(a)//int(b))
        except Exception  as e:
            print("Error Code:",e)
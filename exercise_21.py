"""
    Exercise - 21:  itertools.product()

    Sample Input
    1 2
    3 4

    Sample Output
    (1, 3) (1, 4) (2, 3) (2, 4)
        
    Cassio Cioni Carmo - 04/19/2023
"""
from itertools import product

if __name__ == '__main__':
    x = [int(x) for x in input().split()]
    y = [int(x) for x in input().split()]

    for x in list(product(x,y)):
        print(x, end=" ")
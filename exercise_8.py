"""
   Exercise - 8:  Print a list of all possible coordinates given by (i, j, k)  on a 3D grid where the sum of i + j + k is not equal to n.
   Print the list in lexicographic increasing order.

   Sample Input 0
    1
    1
    1
    2

    Sample Output 0
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

    Sample Input 1
    2
    2
    2
    2

    Sample Output 1
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], 
    [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], 
    [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], 
    [2, 2, 0], [2, 2, 1], [2, 2, 2]]
    
    Cassio Cioni Carmo - 04/06/2023
"""

if __name__ == '__main__':
    numerber_x = int(input())
    numerber_y = int(input())
    numerber_z = int(input())
    numerber_n = int(input())
    
    lst=[]
    
    for i in range(numerber_x + 1):
        for j in range(numerber_y + 1):
            for k in range(numerber_z + 1):
                if i+j+k != numerber_n:
                    lst.append(f"[{i}, {j}, {k}]")

    print("["+", ".join(lst)+"]") 
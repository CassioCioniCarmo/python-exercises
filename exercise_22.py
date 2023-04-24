"""
    Exercise - 22:  Introduction to Sets

    Sample Input
    STDIN                                       Function
    -----                                       --------
    10                                          arr[] size N = 10
    161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]

    Sample Output
    169.375
        
    Cassio Cioni Carmo - 04/23/2023
"""
def average(array):
    array_set = set(array)
    
    return sum(array_set)/len(array_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
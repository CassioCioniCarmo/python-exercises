"""
    Exercise - 19:  Capitalize!

    Sample Input
    chris alan

    Sample Output
    Chris Alan
        
    Cassio Cioni Carmo - 04/17/2023
"""
def solve(string):
    new_tring = string.title()
    return new_tring

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

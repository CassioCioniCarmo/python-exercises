"""
    Exercise - 24:  Designer Door Mat

    Sample Input
    9 27

    Sample Output
    ------------.|.------------
    ---------.|..|..|.---------
    ------.|..|..|..|..|.------
    ---.|..|..|..|..|..|..|.---
    ----------WELCOME----------
    ---.|..|..|..|..|..|..|.---
    ------.|..|..|..|..|.------
    ---------.|..|..|.---------
    ------------.|.------------
        
    Cassio Cioni Carmo - 06/03/2023
"""
m, n = map(int, input().strip().split())
design = '.|.'

for i in range(1, m//2 + 1):
    print((design*(2*i - 1)).center(n, '-'))
print('WELCOME'.center(n, '-'))
for i in range(m//2, 0, -1):
    print((design*(2*i - 1)).center(n, '-'))
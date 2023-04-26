"""
    Exercise - 23:  Polar Coordinates

    Sample Input
    1+2j

    Sample Output
    2.23606797749979 
    1.1071487177940904
        
    Cassio Cioni Carmo - 04/26/2023
"""
import cmath

if __name__ == '__main__':
    n = complex(input())
    
    number_phase = cmath.phase(n)
    number_modulus  = abs(n)

    print(number_modulus)
    print(number_phase)
"""
    Exercise - 13:  What's Your Name?

    Sample Input
    Ross
    Taylor

    Sample Output 
    Hello Ross Taylor! You just delved into python.
        
    Cassio Cioni Carmo - 04/12/2023
"""
def print_full_name(first, last):
    print("Hello " + first +' '+ last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
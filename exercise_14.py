"""
    Exercise - 14:  Mutations

    Sample Input

    STDIN           Function
    -----           --------
    abracadabra     s = 'abracadabra'
    5 k             position = 5, character = 'k'
    Sample Output

    abrackdabra
        
    Cassio Cioni Carmo - 04/13/2023
"""
def mutate_string(string, position, character):
    list_conv = list(string)
    list_conv[position] = character
    return ''.join(list_conv)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
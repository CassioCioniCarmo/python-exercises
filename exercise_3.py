"""
    Exercice - 3: The two numbers calculator
    A python program just to make a operation choosed by the user
    
    Cássio Cioni Carmo - 03/30/2023
"""

if __name__ == "__main__":
    first_num = int(input("Insert the first number:"))
    second_num = int(input("Insert the second number:"))
    operation = input("Choose operation (+ for addition, - for subtraction, * for multiplication and / for division):")
    
    if(operation == "+"):
        print("The result is:", first_num + second_num)
    elif(operation == "-"):
        print("The result is:", first_num - second_num)
    elif(operation == "*"):
        print("The result is:", first_num * second_num)
    elif(operation == "/"):
        print("The result is:", float(first_num / second_num))
    else:
         print("Invalid operation!")

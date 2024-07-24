""" 
Its a a calculator project, it calculates for you the numbers 
you entered based on the operation of your choice, then it will 
ask you to continue and operation with asnwer and number which you 
you will enterif yoou accept
"""
import os
from Arts.CalArt import logo
print(logo)


def add(n1, n2):
    """Addition Method"""
    return n1+n2


def subtract(n1, n2):
    """Subtraction method"""
    return n1-n2


def multiply(n1, n2):
    """Multiplication method"""
    return n1*n2


def divide(n1, n2):
    """ Division method"""
    return n1/n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculetor():
    """ this function calculates two numbers with an operation of your choice"""
    num1 = float(input("What is your first number: "))
    for symbol in operations:
        print(symbol)

    do_again = True
    while do_again:
        operation_symbol = input("Choose an operation: ")
        num2 = float(input("What is your next number: "))

        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} equals to {answer}")
        prompt = input(
            f"Do you want to continue calculating with {answer} type 'Y' to continue or 'N' to start from begining or 'X' to end the app: ").lower()
        if prompt.lower() == 'n':
            do_again = False
            os.system("cls")
            calculetor()
        elif prompt == "x":
            break
        else:
            num1 = answer


calculetor()

# What's the first number? : f_number
# +
# -
# *
# /
# Pick an operation: user_operation
# What's the next number?: s_number
# user_no user_operation next_no
# Type 'y' to continue calculating with result, or type 'n' to start a new calculation

from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


def remainder(n1, n2):
    return n1 % n2

def exponent(n1, n2):
    return n1 ** n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : division,
    '%' : remainder,
    '^' : exponent, 
}

def calculator():
    num1 = float(input("What's the first number? "))
    should_continue = True

    for symbol in operations:
        print(symbol)
    
    while should_continue:

        chosen_symbol = input("Pick an operation? ")

        calculation_operation = operations[chosen_symbol]

        next_num = float(input("What's the next number? "))

        answer = calculation_operation(num1, next_num)

        print(f"{num1} {chosen_symbol} {next_num} : {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation? ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
        

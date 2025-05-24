from colorama import Fore, Style, init
import art

def add(n1,n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(f"{Fore.RED}{art.logo}{Style.RESET_ALL}")
    print("============|| Welcome To My Calculator ||===========")
    should_accumulate = True
    num1 = float(input("What is your first number:-\n"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pic uo operation:-")
        num2 = float(input("what is your next number:-\n"))
        answer = operations[operation_symbol](num1,num2)
        print(f"{Fore.GREEN}Result :- {num1} {operation_symbol} {num2} = {answer}{Style.RESET_ALL}")

        choice = input(f"Type 'Y' to continue with {answer}, or type 'N' to start new calculation:-").lower()

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()


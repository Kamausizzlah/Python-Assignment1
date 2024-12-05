num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Select an operation (+, -, /, *): ")

def calculator():
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Division by zero is not valid")
    else:
        print("Please select a valid operation between +, -, *, /")

calculator()
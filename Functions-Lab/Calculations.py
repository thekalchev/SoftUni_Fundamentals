operation = input()
num1 = int(input())
num2 = int(input())


def calculator(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2


print(int(calculator(operation, num1, num2)))

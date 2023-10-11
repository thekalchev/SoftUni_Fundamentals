def calculator(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return int(num1 / num2)


operation = input()
num1 = int(input())
num2 = int(input())
result = calculator(operation, num1, num2)
print(result)

'''
moje samo s edin dictionary:
def calculator(operation, num1, num2):
    return {'multiply' : num1 * num2,
            'divide': int(num1 / num2)
            'add': num1 + num2
            'subtract': num1 - num2}.get(operation, 'Invalid operation')
'''

# from math import factorial
# def fact(number, number2):
#     factorial_of_number = factorial(number)
#     factorial_of_number2 = factorial(number2)
#     first_divided_by_second = factorial_of_number / factorial_of_number2
#     return first_divided_by_second
#
# num1 = int(input())
# num2 = int(input())
# final_result = fact(num1,num2)
# print(f'{final_result:.2f}')

def calculate_the_factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number  # initial number factorial -> number!


first_number = int(input())
second_number = int(input())

first_number_factorial = calculate_the_factorial(first_number)
second_number_factorial = calculate_the_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f'{result:.2f}')

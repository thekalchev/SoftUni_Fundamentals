# x = int(input())
# y = int(input())
# z = int(input())
# def sum_numbers(x, y, z):
#     return x + y
# result = sum_numbers(x, y, z)
# def subtract(result, z):
#     return result - z
#
# final_result = subtract(result, z)
# print(final_result)

def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))

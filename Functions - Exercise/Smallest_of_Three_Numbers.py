# smallest_of_three_numbers = lambda x, y, z: min(x, y, z)
# x = int(input())
# y = int(input())
# z = int(input())
# print(smallest_of_three_numbers(x, y, z))

# def smallest(some_numbers: list):
#     return min(some_numbers)
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# smallest_element = smallest([first_number, second_number, third_number])
# print(smallest_element)

def smallest(first,second,third): 
    return min(first,second,third)

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest(first_number,second_number,third_number))
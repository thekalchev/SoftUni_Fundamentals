# def copy(string, counter):
#     return string * counter
# string = input()
# counter = int(input())
# result = copy(string, counter)
# print(result)

repeat_string = lambda string, number: string * number
string = input()
number = int(input())
result = repeat_string(string, number)
print(result)
# # number = input()
# # odd_sum = 0
# # even_sum = 0
# # for _ in range(len(number)):
# #     if int(number[_]) % 2 != 0:
# #         odd_sum += int(number[_])
# #     elif int(number[_]) % 2 == 0:
# #         even_sum += int(number[_])
# # print(f'Odd sum = {odd_sum}, Even sum = {even_sum}')
#
# odd_sum = 0
# even_sum = 0
# def odd_number_sum(number):
#     global odd_sum
#     global even_sum
#     for _ in range(len(number)):
#         if int(number[_]) % 2!= 0:
#             odd_sum += int(number[_])
#     return odd_sum
# def even_number_sum(number):
#     global odd_sum
#     global even_sum
#     for _ in range(len(number)):
#         if int(number[_]) % 2 == 0:
#             even_sum += int(number[_])
#     return even_sum
#
# number = input()
# print(f'Odd sum = {odd_number_sum(number)}, Even sum = {even_number_sum(number)}')
#

def odd_even_sums(some_number:str):
    sum_of_even = 0
    sum_of_odd = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return sum_of_odd, sum_of_even


number = input()
sum_of_odd_digits, sum_of_even_digits = odd_even_sums(number)
print(f'Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}')
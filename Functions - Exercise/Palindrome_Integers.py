# nums = input().split(', ')
# for num_as_string in nums:
#     middle = len(num_as_string) // 2
#     first_half = num_as_string[:middle]
#     if len(num_as_string) % 2 == 0:
#         second_half = num_as_string[middle:]
#     elif len(num_as_string) % 2 != 0:
#         second_half = num_as_string[middle + 1:]
#     if first_half == ''.join(reversed(second_half)):
#         print('True')
#     else:
#         print('False')

def is_palindrome(some_number: str) -> bool:
    if some_number == some_number[::-1]:
        return True
    return False


numbers = input().split(', ')
for number in numbers:
    print(is_palindrome(number))
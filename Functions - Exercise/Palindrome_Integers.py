nums = input().split(', ')
for num_as_string in nums:
    middle = len(num_as_string) // 2
    first_half = num_as_string[:middle]
    if len(num_as_string) % 2 == 0:
        second_half = num_as_string[middle:]
    elif len(num_as_string) % 2 != 0:
        second_half = num_as_string[middle + 1:]
    if first_half == ''.join(reversed(second_half)):
        print('True')
    else:
        print('False')
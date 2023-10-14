nums_list = input().split()
nums_list_as_integers = []
for i in nums_list:
    nums_list_as_integers.append(int(i))
print(f'The minimum number is {min(nums_list_as_integers)}')
print(f'The maximum number is {max(nums_list_as_integers)}')
print(f'The sum number is: {sum(nums_list_as_integers)}')

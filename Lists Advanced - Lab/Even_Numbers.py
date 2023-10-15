nums = list(map(int, input().split(', ')))
even_nums_index = []
for index, num in enumerate(nums):
    if num % 2 == 0:
        even_nums_index.append(index)
print(even_nums_index)
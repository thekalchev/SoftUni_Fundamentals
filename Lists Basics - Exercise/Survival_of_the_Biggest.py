list_of_numbers = input().split()
list_of_numbers = list(map(int, list_of_numbers))
numbers_to_remove = int(input())

for i in range(numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))

output = ', '.join(map(str, list_of_numbers))
print(output)
# we use map to convert it to strings, because join doesn't work with integers

list_of_numbers = input().split()
list_of_numbers = list(map(int, list_of_numbers))
numbers_to_remove = int(input())

for i in range(numbers_to_remove):
    if list_of_numbers:
        list_of_numbers.remove(min(list_of_numbers))

output = ', '.join(map(str, list_of_numbers))
print(output)

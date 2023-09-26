num_of_lines = int(input())
positive_numbers = []
negative_numbers = []
sum_of_all_negatives = 0
for _ in range(num_of_lines):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)
for i in range(len(negative_numbers)):
    sum_of_all_negatives += int(negative_numbers[i])
print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {len(positive_numbers)}')
print(f'Sum of negatives: {sum_of_all_negatives}')

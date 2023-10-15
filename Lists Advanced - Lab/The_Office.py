employees_happiness = list(map(int, input().split()))
happiness_factor = int(input())
total_count = len(employees_happiness)
multiplied_happiness = []
for i in employees_happiness:
    multiplied_happiness.append(happiness_factor * i)
average_sum_of_happiness = sum(multiplied_happiness) / total_count
happy_count = [happier for happier in multiplied_happiness if happier >= average_sum_of_happiness]
if len(happy_count) >= total_count / 2:
    print(f'Score: {len(happy_count)}/{total_count}. Employees are happy!')
else:
    print(f'Score: {len(happy_count)}/{total_count}. Employees are not happy!')

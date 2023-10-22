employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students_count = int(input())
hour = 0
while students_count > 0:
    hour += 1
    if hour % 4 == 0:
        continue
    students_count -= employee3 + employee2 + employee1

print(f'Time needed: {hour}h.')


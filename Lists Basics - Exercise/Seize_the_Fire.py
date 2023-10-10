level_of_fire = input().split('#')
amount_of_water = int(input())
effort = 0
total_fire = 0
print('Cells:')
for fire in range(len(level_of_fire)):
    level, value = level_of_fire[fire].split(' = ')
    value = int(value)
    if level == 'High':
        if 81 <= value <= 125:
            if amount_of_water >= value:
                amount_of_water -= value
                effort += value * .25
                total_fire += value
                print(f' - {value}')
    if level == 'Medium':
        if 51 <= value <= 80:
            if amount_of_water >= value:
                amount_of_water -= value
                effort += value * .25
                total_fire += value
                print(f' - {value}')
    if level == 'Low':
        if 1 <= value <= 50:
            if amount_of_water >= value:
                amount_of_water -= value
                effort += value * .25
                total_fire += value
                print(f' - {value}')
    else:
        continue
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
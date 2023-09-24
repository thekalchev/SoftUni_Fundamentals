water_tank_capacity = 255
lines = int(input())
liters_total = 0
for i in range(lines):
    liters = int(input())
    liters_total += liters
    if liters_total > water_tank_capacity:
        print(f'Insufficient capacity!')
        liters_total -= liters
print(f'{liters_total}')

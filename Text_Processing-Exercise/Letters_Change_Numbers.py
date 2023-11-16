sequence = input().strip().split()
total_sum = 0
divider_multiplier = 0
add_subtract = 0
number_to_use = ''
for part in sequence:
    for char in part:
        if char.isnumeric():
            number_to_use += char
    if part[0].islower():
        divider_multiplier = ord(part[0]) - 96
        total_sum += int(number_to_use) * divider_multiplier
    else:
        divider_multiplier = ord(part[0]) - 64
        total_sum += int(number_to_use) / divider_multiplier
    if part[-1].islower():
        add_subtract = ord(part[-1]) - 96
        total_sum += add_subtract
    else:
        add_subtract = ord(part[-1]) - 64
        total_sum -= add_subtract
    divider_multiplier = 0
    add_subtract = 0
    number_to_use = ''
print(f'{total_sum:.2f}')



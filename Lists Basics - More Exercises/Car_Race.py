times = input().split()
left = 0
right = 0
middle = len(times) // 2
for time in times[:middle]:
    time = int(time)
    if time != 0:
        left += time
    else:
        left *= .8
for time in times[middle:]:
    time = int(time)
    if time != 0:
        right += time
    else:
        right *= .8
if left < right:
    print(f'The winner is left with total time: {left:.1f}')
else:
    print(f'The winner is right with total time: {right:.1f}')

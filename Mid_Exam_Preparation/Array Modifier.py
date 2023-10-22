array = list(map(int, input().split()))
while True:
    command = input().split()
    if command[0] == 'end':
        break
    action = command[0]
    if action == 'swap':
        index1 = int(command[1])
        index2 = int(command[2])
        array[index1], array[index2] = array[index2], array[index1]
    if action == 'multiply':
        index1 = int(command[1])
        index2 = int(command[2])
        array[index1] = array[index1] * array[index2]
    if action == 'decrease':
        for a in range(len(array)):
            array[a] -= 1
print(', '.join(map(str, array)))


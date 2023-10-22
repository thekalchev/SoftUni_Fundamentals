sequence = list(map(int, input().split()))
while True:
    command = input().split()
    if command[0] == 'Finish':
        break
    action = command[0]
    value = int(command[1])
    if action == 'Add':
        sequence.append(value)
    elif action == 'Remove':
        if value in sequence:
            sequence.remove(value)
    elif action == 'Replace':
        replacement = int(command[2])
        if value in sequence:
            index = sequence.index(value)
            sequence.pop(index)
            sequence.insert(index, replacement)
    elif action == 'Collapse':
        sequence = [num for num in sequence if num >= value]
print(' '.join(map(str, sequence)))


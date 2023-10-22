targets_list = list(map(int, input().split()))
while True:
    command = input()
    if command == 'End':
        print('|'.join(map(str, targets_list)))
        break
    current_command = command.split()
    action = current_command[0]
    index = int(current_command[1])
    num = int(current_command[2])
    if action == 'Shoot':
        if 0 <= index <= len(targets_list):
            targets_list[index] -= num
            if targets_list[index] <= 0:
                targets_list.remove(targets_list[index])

    elif action == 'Add':
        if 0 <= index < len(targets_list):
            targets_list.insert(index, num)
        else:
            print(f'Invalid placement!')

    elif action == 'Strike':
        if 1 < index < len(targets_list) - 1:
            targets_list.pop(index + 1)
            targets_list.pop(index)
            targets_list.pop(index - 1)
        else:
            print(f'Strike missed!')


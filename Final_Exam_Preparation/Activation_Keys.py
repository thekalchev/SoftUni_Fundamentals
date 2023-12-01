raw_activation_key = input()
while True:
    command = input().split('>>>'
                            )
    if command[0] == 'Generate':
        print(f'Your activation key is: {raw_activation_key}')
        break
    elif command[0] == 'Contains':
        substring = command[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print(f'Substring not found!')
    elif command[0] == 'Flip':
        case, start_index, end_index = command[1], int(command[2]), int(command[3])
        if case == 'Upper':
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[
                                                                    start_index:end_index].upper() + raw_activation_key[
                                                                                                     end_index:]

        elif case == 'Lower':
            raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[
                                                                    start_index:end_index].lower() + raw_activation_key[
                                                                                                     end_index:]
        print(raw_activation_key)
    elif command[0] == 'Slice':
        start, end = int(command[1]), int(command[2])
        raw_activation_key = raw_activation_key[:start] + raw_activation_key[end:]
        print(raw_activation_key)

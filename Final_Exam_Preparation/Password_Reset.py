password = input()
while True:
    command = input().split()
    if command[0] == 'Done':
        print(f'Your password is: {password}')
        break
    action = command[0]
    if action == 'TakeOdd':
        password = password[1::2]
        print(password)
    elif action == 'Cut':
        index, length = int(command[1]), int(command[2])
        substring = password[index:index+length]
        password = password.replace(substring, '')
        print(password)
    elif action == 'Substitute':
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print(f'Nothing to replace!')
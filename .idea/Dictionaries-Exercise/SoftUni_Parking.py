num_of_commands = int(input())
registration_book = {}
for command in range(num_of_commands):
    command = input().split()
    if len(command) == 3:
        action, name, plate = command
        if name in registration_book:
            print(f'ERROR: already registered with plate number {plate}')
        else:
            registration_book[name] = plate
            print(f'{name} registered {plate} successfully')

    elif len(command) == 2:
        action, name = command
        if name not in registration_book:
            print(f'ERROR: user {name} not found')
        else:
            print(f'{name} unregistered successfully')
            del registration_book[name]

for name, plate in registration_book.items():
    print(f'{name} => {plate}')

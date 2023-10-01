gifts = input().split()

while True:
    command = input().split()
    if command[0] == 'No' and command[1] == 'Money':
        break
    if command[0] == 'OutOfStock':
        gift_to_remove = command[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_remove:
                gifts[i] = 'None'

    elif command[0] == 'Required':
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]

filtered_gifts = [gift for gift in gifts if gift != 'None']
print(' '.join(filtered_gifts))

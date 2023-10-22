items = input().split(', ')
while True:
    command = input()
    if command == 'Craft!':
        break
    action = command.split(' - ')
    current_action = action[0]
    item = action[1]

    if current_action == 'Collect':
        if item not in items:
            items.append(item)
    elif current_action == 'Drop':
        if item in items:
            items.remove(item)
    elif current_action == 'Combine Items':
        item1, item2 = item.split(':')
        if item1 in items:
            index = items.index(item1)
            items.insert(index + 1, item2)
    elif current_action == 'Renew':
        if item in items:
            items.remove(item)
            items.append(item)
print(', '.join(items))

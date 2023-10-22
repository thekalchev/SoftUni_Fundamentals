phones_list = input().split(', ')
while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    action = command[0]
    type_of_phone = command[1]
    if action == 'Add':
        if type_of_phone not in phones_list:
            phones_list.append(type_of_phone)
    elif action == 'Remove':
        if type_of_phone in phones_list:
            phones_list.remove(type_of_phone)
    elif action == 'Bonus phone':
        old_phone, new_phone = type_of_phone.split(':')
        if old_phone in phones_list:
            index = phones_list.index(old_phone)
            phones_list.insert(index + 1, new_phone)
    elif action == 'Last':
        if type_of_phone in phones_list:
            phones_list.remove(type_of_phone)
            phones_list.append(type_of_phone)
print(', '.join(phones_list))

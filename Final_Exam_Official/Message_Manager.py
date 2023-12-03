capacity = int(input())
messages_info = {}

while True:
    command = input().split('=')

    if command[0] == 'Statistics':
        break

    username = command[1]

    if command[0] == 'Add':
        sent = int(command[2])
        received = int(command[3])
        if username not in messages_info:
            messages_info[username] = {'sent': sent, 'received': received}

    elif command[0] == 'Message':
        sender = command[1]
        receiver = command[2]
        if sender in messages_info and receiver in messages_info:
            messages_info[sender]['sent'] += 1
            messages_info[receiver]['received'] += 1
            if messages_info[sender]['sent'] + messages_info[sender]['received'] == capacity:
                del messages_info[sender]
                print(f"{sender} reached the capacity!")
            if messages_info[receiver]['sent'] + messages_info[receiver]['received'] == capacity:
                del messages_info[receiver]
                print(f"{receiver} reached the capacity!")

    elif command[0] == 'Empty':
        if username == 'All':
            messages_info.clear()
        elif username in messages_info:
            del messages_info[username]

print(f"Users count: {len(messages_info)}")
for user, info in messages_info.items():
    print(f"{user} - {info['sent'] + info['received']}")

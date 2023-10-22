initial_health = 100
initial_bitcoins = 0
dungeon_rooms = input().split('|')
health = initial_health
bitcoins = initial_bitcoins

for room in range(len(dungeon_rooms)):
    dungeon_room = dungeon_rooms[room].split()
    command = dungeon_room[0]
    number = int(dungeon_room[1])

    if command == 'potion':
        if (health + number) < initial_health:
            health += number
            print(f'You healed for {number} hp.')
            print(f'Current health: {health} hp.')
        else:
            amount_healed = 100 - health
            health = 100
            print(f'You healed for {amount_healed} hp.')
            print(f'Current health: {health} hp.')

    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')

    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        if health <= 0:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {room + 1}')
            exit()

print(f"You've made it!")
print(f'Bitcoins: {bitcoins}')
print(f'Health: {health}')

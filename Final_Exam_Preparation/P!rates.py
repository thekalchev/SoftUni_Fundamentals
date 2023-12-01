cities = {}
while True:
    command = input().split('||')
    if command[0] == 'Sail':
        break
    city_name = command[0]
    population = int(command[1])
    gold = int(command[2])
    if city_name not in cities:
        cities[city_name] = [population, gold]
    elif city_name in cities:
        cities[city_name][0] += population
        cities[city_name][1] += gold
while True:
    command = input().split('=>')
    if command[0] == 'End':
        break
    elif command[0] == 'Plunder':
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        cities[town][0] -= people
        cities[town][1] -= gold
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
            print(f'{town} has been wiped off the map!')
            del cities[town]
        else:
            print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
    elif command[0] == 'Prosper':
        town = command[1]
        gold = int(command[2])
        if gold >= 0:
            cities[town][1] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.')
        else:
            print(f'Gold added cannot be a negative number!')
            continue
print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
for city in cities:
    print(f'{city} -> Population: {cities[city][0]} citizens, '
          f'Gold: {cities[city][1]} kg')

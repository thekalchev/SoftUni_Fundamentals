# cities = {}
# while True:
#     command = input().split('||')
#     if command[0] == 'Sail':
#         break
#     city_name = command[0]
#     population = int(command[1])
#     gold = int(command[2])
#     if city_name not in cities:
#         cities[city_name] = [population, gold]
#     elif city_name in cities:
#         cities[city_name][0] += population
#         cities[city_name][1] += gold
# while True:
#     command = input().split('=>')
#     if command[0] == 'End':
#         break
#     elif command[0] == 'Plunder':
#         town = command[1]
#         people = int(command[2])
#         gold = int(command[3])
#         cities[town][0] -= people
#         cities[town][1] -= gold
#         if cities[town][0] <= 0 or cities[town][1] <= 0:
#             print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
#             print(f'{town} has been wiped off the map!')
#             del cities[town]
#         else:
#             print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
#     elif command[0] == 'Prosper':
#         town = command[1]
#         gold = int(command[2])
#         if gold >= 0:
#             cities[town][1] += gold
#             print(f'{gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.')
#         else:
#             print(f'Gold added cannot be a negative number!')
#             continue
# print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
# for city in cities:
#     print(f'{city} -> Population: {cities[city][0]} citizens, '
#           f'Gold: {cities[city][1]} kg')

cities = {}
while True:
    command = input().split('||')
    if command[0] == 'Sail':
        break
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities:
        cities[city] = {'population': 0, 'gold': 0}
    cities[city]['population'] += population
    cities[city]['gold'] += gold

command = input().split('=>')
while command[0] != 'End':
    action = command[0]
    if action == 'Plunder':
        town, people, gold = command[1], int(command[2]), int(command[3])
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        if cities[town]['population'] == 0 or cities[town]['gold'] == 0:
            cities.pop(town)
            print(f'{town} has been wiped off the map!')
    elif action == 'Prosper':
        town, gold = command[1], int(command[2])
        if gold < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            cities[town]['gold'] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')

    command = input().split('=>')

if cities:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for town, town_information in cities.items():
        print(f'{town} -> Population: {town_information["population"]} citizens, Gold: {town_information["gold"]} kg')

else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
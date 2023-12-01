# cars = {}
# num_of_cars = int(input())
# for current_car in range(num_of_cars):
#     car, milage, fuel = input().split('|')
#     cars[car] = [int(milage), int(fuel)]
#
# while True:
#     command = input().split(' : ')
#     if command[0] == 'Stop':
#         for car in cars:
#             print(f'{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.')
#         break
#     elif command[0] == 'Drive':
#         car, distance, fuel = command[1], int(command[2]), int(command[3])
#         if cars[car][1] < fuel:
#             print('Not enough fuel to make that ride')
#         else:
#             cars[car][0] += distance
#             cars[car][1] -= fuel
#             print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
#         if cars[car][0] >= 100000:
#             print(f'Time to sell the {car}!')
#             del cars[car]
#     elif command[0] == 'Refuel':
#         car, fuel = command[1], int(command[2])
#         if (cars[car][1] + fuel) > 75:
#             cars[car][1] = 75
#             print(f'{car} refueled with {75 - cars[car][1]} liters')
#         else:
#             cars[car][1] += fuel
#             print(f'{car} refueled with {fuel} liters')
#     elif command[0] == 'Revert':
#         car, kilometers = command[1], int(command[2])
#         cars[car][0] -= kilometers
#         if cars[car][0] < 10000:
#             cars[car][0] = 10000
#         else:
#             print(f'{car} mileage decreased by {kilometers} kilometers')
def create_car(name, milage, fuel):
    return {'name': name, 'mileage': milage, 'fuel': fuel}


def drive(car, distance, required_fuel):
    if car['fuel'] >= required_fuel:
        car['mileage'] += distance
        car['fuel'] -= required_fuel
        print(f'{car["name"]} driven for {distance} kilometers. {required_fuel} liters of fuel consumed.')
        if car['mileage'] >= 100000:
            print(f'Time to sell the {car["name"]}!')
            return True
    else:
        print('Not enough fuel to make that ride')
    return False


def refuel(car, added_fuel):
    max_fuel = 75
    fuel_to_add = min(added_fuel, max_fuel - car['fuel'])
    car['fuel'] += fuel_to_add
    print(f'{car["name"]} refueled with {fuel_to_add} liters')


def revert(car, kilometers):
    car['mileage'] -= kilometers
    if car['mileage'] < 10000:
        car['mileage'] = 10000
    else:
        print(f'{car["name"]} mileage decreased by {kilometers} kilometers')


def main_function():
    n = int(input())
    cars = []

    for _ in range(n):
        car_info = input().split('|')
        car = create_car(car_info[0], int(car_info[1]), int(car_info[2]))
        cars.append(car)

    while True:
        command = input().split(' : ')

        if command[0] == 'Stop':
            break

        action = command[0]
        car_name = command[1]

        for car in cars:
            if car['name'] == car_name:
                if action == 'Drive':
                    distance = int(command[2])
                    fuel = int(command[3])
                    if drive(car, distance, fuel):
                        cars.remove(car)

                elif action == 'Refuel':
                    added_fuel = int(command[2])
                    refuel(car, added_fuel)

                elif action == 'Revert':
                    kilometers = int(command[2])
                    revert(car, kilometers)
    for car in cars:
        print(f'{car["name"]} -> Mileage: {car["mileage"]} kms, Fuel in the tank: {car["fuel"]} lt.')

main_function()

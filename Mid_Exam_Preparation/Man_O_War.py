# pirate_ship_status = list(map(int, input().split(">")))
# warship_status = list(map(int, input().split(">")))
# maximum_health = int(input())
#
# while True:
#     command = input()
#
#     if command == "Retire":
#         break
#
#     instructions = command.split()
#     action = instructions[0]
#
#     if action == "Fire":
#         index = int(instructions[1])
#         damage = int(instructions[2])
#
#         if 0 <= index < len(warship_status):
#             warship_status[index] -= damage
#
#             if warship_status[index] <= 0:
#                 print("You won! The enemy ship has sunken.")
#                 exit()
#
#     elif action == "Defend":
#         start_index = int(instructions[1])
#         end_index = int(instructions[2])
#         damage = int(instructions[3])
#
#         if 0 <= start_index <= end_index < len(pirate_ship_status):
#             for i in range(start_index, end_index + 1):
#                 pirate_ship_status[i] -= damage
#
#                 if pirate_ship_status[i] <= 0:
#                     print("You lost! The pirate ship has sunken.")
#                     exit()
#
#     elif action == "Repair":
#         index = int(instructions[1])
#         health = int(instructions[2])
#
#         if 0 <= index < len(pirate_ship_status):
#             pirate_ship_status[index] = min(pirate_ship_status[index] + health, maximum_health)
#
#     elif action == "Status":
#         count = sum(1 for section in pirate_ship_status if section < 0.2 * maximum_health)
#         print(f"{count} sections need repair.")
#
# pirate_ship_status_status = sum(pirate_ship_status)
# warship_status_status = sum(warship_status)
# print(f"Pirate ship status: {pirate_ship_status_status}")
# print(f"Warship status: {warship_status_status}")

def fire_func(warship, index, damage):
    if 0 <= index < len(warship):
        warship[index] -= damage

        if warship[index] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()


def defend_func(pirate_ship, startIndex, endIndex, damage):
    if 0 <= startIndex < len(pirate_ship) and 0 <= endIndex < len(pirate_ship):
        for i in range(startIndex, endIndex + 1):
            pirate_ship[i] -= damage

            if pirate_ship[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()


def repair_func(pirate_ship, index, health, max_health):
    if 0 <= index <= len(pirate_ship):
        pirate_ship[index] = min(pirate_ship[index] + health, max_health)

def status_func(pirate_ship, max_health):
    count = sum(1 for section in pirate_ship if section < 0.2 * max_health)
    print(f'{count} sections need repair.')


pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split('>')))
max_health = int(input())

while True:
    command = input().split()
    current_command = command[0]

    if current_command == 'Retire':
        break

    elif current_command == 'Fire':
        index, damage = int(command[1]), int(command[2])
        fire_func(warship, index, damage)

    elif current_command == 'Defend':
        startIndex, endIndex, damage = int(command[1]), int(command[2]), int(command[3])
        defend_func(pirate_ship, startIndex, endIndex, damage)

    elif current_command == 'Repair':
        index, health = int(command[1]), int(command[2])
        repair_func(pirate_ship, index, health, max_health)

    elif current_command == 'Status':
        status_func(pirate_ship, max_health)

print(f'Pirate ship status: {sum(pirate_ship)}')
print(f'Warship status: {sum(warship)}')

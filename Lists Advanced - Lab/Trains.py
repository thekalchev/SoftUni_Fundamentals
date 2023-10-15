# number_of_wagons = int(input())
# train_wagons = []
# for wagon in range(number_of_wagons):
#     train_wagons.append(0)
# while True:
#     command = input()
#     move_people = command.split()
#     if command == 'End':
#         break
#     elif move_people[0] == 'add':
#         train_wagons[-1] += int(move_people[1])
#     elif move_people[0] == 'insert':
#         train_wagons[int(move_people[1])] += int(move_people[2])
#     elif move_people[0] == 'leave':
#         train_wagons[int(move_people[1])] -= int(move_people[2])
# print(train_wagons)

wagons = [0] * int(input())
while True:
    command = input().split()
    if command[0] == 'End':
        print(wagons)
        break
    elif command[0] == 'add':
        number_of_people = int(command[1])
        wagons[-1] += number_of_people
    elif command[0] == 'insert':
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif command[0] == 'leave':
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people


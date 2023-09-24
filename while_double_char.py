# command = input()
# while command != 'End':
#     if command == 'SoftUni':
#         command = input()
#         continue
#     for i in command:
#         print(i * 2, end='')
#     print()
#     command = input()
current_string = input()
while current_string != 'End':
    if current_string != 'SoftUni':
        new_string = ''
        for character in current_string:
            new_string += character * 2
        print(new_string)
    current_string = input()

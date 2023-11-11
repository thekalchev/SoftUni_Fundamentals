# phonebook = {}
# while True:
#     message = input()
#     if '-' in message:
#         person, phone_number = message.split('-')
#         phonebook[person] = phone_number
#     elif message.isnumeric():
#         for _ in range(int(message)):
#             search_for = input()
#             if search_for in phonebook:
#                 print(f'{search_for} -> {phonebook[search_for]}')
#             else:
#                 print(f'Contact {search_for} does not exist.')
#         break

phonebook = {}
while True:
    entry = input()
    if '-' not in entry:
        break
    name, phone_number = entry.split('-')
    phonebook[name] = phone_number
searches = int(entry)
for search in range(searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
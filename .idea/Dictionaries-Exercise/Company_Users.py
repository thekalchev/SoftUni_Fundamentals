book = {}
while True:
    command = input()
    if command == 'End':
        break
    company_name, id = command.split(' -> ')
    if company_name not in book:
        book[company_name] = []
    if id not in book[company_name]:
        book[company_name].append(id)
for company, id in book.items():
    print(f'{company}')
    for id in id:
        print(f'-- {id}')
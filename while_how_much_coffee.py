coffees = 0
while True:
    command = input()
    if command == 'END':
        break
    if command.lower() != 'coding' and command.lower() != 'dog' and command.lower() != 'cat' and command.lower() != 'movie':
        continue
    if command.isupper():
        coffees += 2
    else:
        coffees += 1
if coffees > 5:
    print('You need extra sleep')
else:
    print(coffees)

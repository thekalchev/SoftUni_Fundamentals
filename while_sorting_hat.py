team = ''
while True:
    name = input()
    if name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    if name == 'Voldemort':
        print('You must not speak of that name!')
        exit()
    if len(name) < 5:
        team = 'Gryffindor'
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        team = 'Slytherin'
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        team = 'Ravenclaw'
        print(f'{name} goes to Ravenclaw.')
    elif len(name) > 6:
        team = 'Hufflepuff'
        print(f'{name} goes to Hufflepuff.')

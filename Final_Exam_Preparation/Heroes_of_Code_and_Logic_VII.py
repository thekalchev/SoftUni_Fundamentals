number_of_heroes = int(input())
heroes_info = {}
for hero in range(number_of_heroes):
    hero_name, HP, MP = current_hero = input().split()
    if int(HP) <= 100 and int(MP) <= 200:
        heroes_info[hero_name] = {'HP': int(HP), 'MP': int(MP)}

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break

    action = command[0]
    hero_name = command[1]

    if action == 'CastSpell':
        MP_needed, spell_name = int(command[2]), command[3]
        if MP_needed <= heroes_info[hero_name]['MP']:
            heroes_info[hero_name]['MP'] -= MP_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes_info[hero_name]["MP"]} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')

    elif action == 'TakeDamage':
        damage, attacker = int(command[2]), command[3]
        heroes_info[hero_name]['HP'] -= damage
        if heroes_info[hero_name]['HP'] > 0:
            print(f'{hero_name} was hit for {damage} HP by {attacker} '
                  f'and now has {heroes_info[hero_name]["HP"]} HP left!')
        else:
            print(f'{hero_name} has been killed by {attacker}!')
            del heroes_info[hero_name]

    elif action == 'Recharge':
        amount = int(command[2])
        heroes_info[hero_name]['MP'] += amount
        if heroes_info[hero_name]['MP'] > 200:
            amount_recharged = 200 - heroes_info[hero_name]['MP'] + amount
            heroes_info[hero_name]["MP"] = 200
            print(f'{hero_name} recharged for {amount_recharged} MP!')
        else:
            print(f'{hero_name} recharged for {amount} MP!')

    elif action == 'Heal':
        amount = int(command[2])
        heroes_info[hero_name]['HP'] += amount
        if heroes_info[hero_name]['HP'] > 100:
            amount_recharged = 100 - heroes_info[hero_name]['HP'] + amount
            heroes_info[hero_name]["HP"] = 100
            print(f'{hero_name} healed for {amount_recharged} HP!')
        else:
            print(f'{hero_name} healed for {amount} HP!')

if heroes_info:
    for hero, hero_information in heroes_info.items():
        print(f'{hero}')
        print(f'  HP: {hero_information["HP"]}')
        print(f'  MP: {hero_information["MP"]}')

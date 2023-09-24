from math import floor

number_of_companions = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        number_of_companions -= 2
    if day % 15 == 0:
        number_of_companions += 5
    coins += 50
    coins -= (2 * number_of_companions)
    if day % 3 == 0:
        coins -= 3 * number_of_companions
    if day % 5 == 0:
        coins += 20 * number_of_companions
        if day % 3 == 0:
            coins -= 2 * number_of_companions
coins_each = coins/number_of_companions
print(f'{number_of_companions} companions received {floor(coins_each)} coins each.')

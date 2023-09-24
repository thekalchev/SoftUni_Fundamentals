budget = int(input())
total_price = 0
while True:
    command = input()
    if command == 'End':
        print('You bought everything needed.')
        break
    price = int(command)
    total_price += price
    if budget < total_price:
        print('You went in overdraft!')
        exit()



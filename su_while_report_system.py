amount_needed = int(input())
command = input()
cash = 0
card = 0
cash_count = 0
card_count = 0
counter = 0
while True:
    if command == 'End':
        print(f'Failed to collect required money for charity.')
        break
    amount = int(command)
    counter += 1
    if counter % 2 == 0:
        if amount < 10:
            print(f'Error in transaction!')
        else:
            print(f'Product sold!')
            card += amount
            card_count += 1
    elif counter % 2 != 0:
        if amount > 100:
            print(f'Error in transaction!')
        else:
            print(f'Product sold!')
            cash += amount
            cash_count += 1
    if cash + card >= amount_needed:
        average_cash = cash / cash_count
        average_card = card / card_count
        print(f'Average CS: {average_cash:.2f}')
        print(f'Average CC: {average_card:.2f}')
        break
    command = input()




train_tickets = 150
items = input().split('|')
budget = float(input())
profit = 0
total_money = 0
for item in range(len(items)):
    type_of_item, price_of_item = items[item].split('->')
    price_of_item = float(price_of_item)
    if type_of_item == 'Clothes':
        if 0 <= price_of_item <= 50.00:
            if budget >= price_of_item:
                budget -= price_of_item
                new_price = price_of_item + price_of_item * .4
                total_money += new_price
                print(f'{new_price:.2f} ', end='')
                profit += new_price - price_of_item
    if type_of_item == 'Shoes':
        if 0 <= price_of_item <= 35.00:
            if budget >= price_of_item:
                budget -= price_of_item
                new_price = price_of_item + price_of_item * .4
                total_money += new_price
                print(f'{new_price:.2f} ',end='')
                profit += new_price - price_of_item
    if type_of_item == 'Accessories':
        if 0 <= price_of_item <= 20.50:
            if budget >= price_of_item:
                budget -= price_of_item
                new_price = price_of_item + price_of_item * .4
                total_money += new_price
                print(f'{new_price:.2f}',end='')
                profit += new_price - price_of_item
print()
print(f'Profit: {profit:.2f}')
if total_money + budget >= train_tickets:
    print('Hello, France!')
else:
    print('Not enough money.')

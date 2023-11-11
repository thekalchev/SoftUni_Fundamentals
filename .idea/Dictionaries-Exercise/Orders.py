information = {}
while True:
    command = input()
    if command == 'buy':
        break
    name, price, quantity = command.split()
    price = float(price)
    quantity = float(quantity)
    if name not in information:
        information[name] = {'price': price, 'quantity': quantity}
    else:
        information[name]['quantity'] += quantity
        if information[name]['price'] != price:
            information[name]['price'] = price
print(information)
for item, cash in information.items():
    total = cash['price'] * cash['quantity']
    print(f'{item} -> {total:.2f}')
price = 0
product = input()
quantity = int(input())

def total_price(product, quantity):
    global price
    if product == 'coffee':
        price = 1.5 * quantity
    elif product == 'water':
        price = 1 * quantity
    elif product == 'coke':
        price = 1.4 * quantity
    elif product == 'snacks':
        price = 2 * quantity
    return f'{price:.2f}'

print(total_price(product, quantity))

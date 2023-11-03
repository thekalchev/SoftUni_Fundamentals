data = input().split()
ask = input().split()
stock = {}
for i in range(0, len(data), 2):
    keys = data[i]
    values = int(data[i + 1])
    stock[keys] = values
for product in ask:
    if product in stock.keys():
        print(f'We have {stock[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")
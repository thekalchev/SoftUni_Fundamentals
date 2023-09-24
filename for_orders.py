orders_count = int(input())
order_price = 0
total_price = 0
for order in range(orders_count):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule < .01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    order_price = price_per_capsule * capsules_needed_per_day * days
    total_price += order_price
    print(f'The price for the coffee is: ${order_price:.2f}')
    order_price = 0

print(f'Total: ${total_price:.2f}')
movie = input()
package = input()
tickets_count = int(input())
total_price = 0
if movie == 'John Wick':
    if package == 'Drink':
        total_price += 12
    elif package == 'Popcorn':
        total_price += 15
    elif package == 'Menu':
        total_price += 19
elif movie == 'Star Wars':
    if package == 'Drink':
        total_price += 18
    elif package == 'Popcorn':
        total_price += 25
    elif package == 'Menu':
        total_price += 30
elif movie == 'Jumanji':
    if package == 'Drink':
        total_price += 9
    elif package == 'Popcorn':
        total_price += 11
    elif package == 'Menu':
        total_price += 14

if movie == 'Star Wars' and tickets_count >= 4:
    total_price *= .7
elif movie == 'Jumanji' and tickets_count == 2:
    total_price *= .85
final_price = total_price * tickets_count
print(f'Your bill is {final_price:.2f} leva.')

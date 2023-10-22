number_of_cities = int(input())
total_profit = 0
for city_num in range(1, number_of_cities + 1):
    city_name = input()
    owners_income = float(input())
    owners_expenses = float(input())
    if city_num % 5 == 0:
        income_loss = owners_income * 0.10
        current_city_profit = owners_income - (owners_expenses + income_loss)
    elif city_num % 3 == 0:
        special_event_costs = owners_expenses * 0.50
        current_city_profit = owners_income - (owners_expenses + special_event_costs)
    else:
        current_city_profit = owners_income - owners_expenses

    print(f'In {city_name} Burger Bus earned {current_city_profit:.2f} leva.')
    total_profit += current_city_profit

print(f'Burger Bus total profit: {total_profit:.2f} leva.')



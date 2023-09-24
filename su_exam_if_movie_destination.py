movie_budget = float(input())
destination = input()
season = input() #Summer/Winter
days_count = int(input())
spent = 0
if destination == 'Dubai':
    if season == 'Winter':
        spent += 45000
    elif season == 'Summer':
        spent += 40000
elif destination == 'Sofia':
    if season == 'Winter':
        spent += 17000
    elif season == 'Summer':
        spent += 12500
elif destination == 'London':
    if season == 'Winter':
        spent += 24000
    elif season == 'Summer':
        spent += 20250
total_spent = days_count * spent
if destination == 'Dubai':
    total_spent *= .7
elif destination == 'Sofia':
    total_spent *= 1.25
if movie_budget >= total_spent:
    print(f'The budget for the movie is enough! We have {movie_budget-total_spent:.2f} leva left!')
else:
    print(f'The director needs {total_spent-movie_budget:.2f} leva more!')


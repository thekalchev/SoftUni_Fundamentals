hall_capacity = int(input())
cash_made = 0
total_visitors = 0
while True:
    command = input()
    if command == 'Movie time!':
        break
    visitors = int(command)
    total_visitors += visitors
    if total_visitors > hall_capacity:
        break
    ticket_price = 5
    if visitors % 3 == 0:
        cash_made += visitors * ticket_price - 5
    else:
        cash_made += visitors * ticket_price
if total_visitors > hall_capacity:
    print(f'The cinema is full.')
else:
    print(f'There are {hall_capacity - total_visitors} seats left in the cinema.')
print(f'Cinema income - {cash_made} lv.')

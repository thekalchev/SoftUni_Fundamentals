# bottle contains 750ml detergent
# 1 plate needs 5ml
# 1 pot needs 15ml
# every third refill is just pots
# other is just plates

bottles_count = int(input())
bottle_capacity = 750
detergent_quantity = bottles_count * bottle_capacity
command = input()
refill = 0
plates = 0
pots = 0

while True:
    if command == 'End':
        break
    dishes_count = int(command)
    refill += 1
    if refill % 3 == 0:
        detergent_quantity -= dishes_count * 15
        pots += dishes_count
    else:
        detergent_quantity -= dishes_count * 5
        plates += dishes_count
    if detergent_quantity < 0:
        print(f'Not enough detergent, {detergent_quantity * -1} ml. more necessary!')
        exit()
    command = input()
print(f'Detergent was enough!')
print(f'{plates} dishes and {pots} pots were washed.')
print(f'Leftover detergent {detergent_quantity} ml.')
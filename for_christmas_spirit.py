quantity_of_decorations = int(input())  # 1-100
remaining_days = int(input())  # 1-100
ornament_set_price = 0
tree_skirt_price = 0
tree_garland_price = 0
tree_lights_price = 0
total_spirit = 0
for day in range(1, remaining_days + 1):
    remaining_days -= 1
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        ornament_set_price += 2 * quantity_of_decorations
        total_spirit += 5
    if day % 3 == 0:
        tree_skirt_price += 5 * quantity_of_decorations
        tree_garland_price += 3 * quantity_of_decorations
        total_spirit += 13
    if day % 5 == 0:
        tree_lights_price += 15 * quantity_of_decorations
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        tree_skirt_price += 5
        tree_garland_price += 3
        tree_lights_price += 15
        if remaining_days == 0:
            total_spirit -= 30

budget = tree_lights_price + tree_garland_price + tree_skirt_price + ornament_set_price
print(f'Total cost: {budget}')
print(f'Total spirit: {total_spirit}')

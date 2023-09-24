budget = float(input())
flour_price_per_kg = float(input())
eggs_price_per_pack = 0.75 * flour_price_per_kg
milk_price_per_liter = 1.25 * flour_price_per_kg
total_for_one_loaf = flour_price_per_kg + eggs_price_per_pack + (0.25 * milk_price_per_liter)
loaves = 0
colored_eggs = 0

while budget >= total_for_one_loaf:
    budget -= total_for_one_loaf  # Deduct the cost of ingredients
    colored_eggs += 3  # Add 3 colored eggs for each loaf
    loaves += 1

    if loaves % 3 == 0:
        lost_eggs = loaves - 2
        colored_eggs -= lost_eggs

money_left = format(budget, ".2f")
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left.")

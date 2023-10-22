food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
guinea_weight = float(input())
day = 0
while food_quantity >= 0.3 and hay_quantity >= 0 and cover_quantity >= 0:
    day += 1
    food_quantity -= .300
    if day % 2 == 0:
        hay_quantity -= food_quantity*.05
    if day % 3 == 0:
        cover_quantity -= guinea_weight * (1/3)
    if day == 30:
        print(f'Everything is fine! Puppy is happy! Food:'
              f' {food_quantity:.2f}, Hay: {hay_quantity:.2f},'
              f' Cover: {cover_quantity:.2f}.')
        exit()
print(f'Merry must go to the pet store!')
# food = input().split()
# keys = []
# values = []
# for i in range(len(food)):
#     if i % 2 == 0:
#         keys.append(food[i])
#     elif i % 2 != 0:
#         values.append(int(food[i]))
# food_dict = dict(zip(keys, values))
# print(food_dict)

data = input().split()
stock = {}
for i in range(0, len(data), 2):
    food = data[i]
    quantity = int(data[i + 1])
    stock[food] = quantity
print(stock)

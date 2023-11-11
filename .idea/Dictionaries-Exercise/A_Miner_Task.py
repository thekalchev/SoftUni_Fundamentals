# book = {}
#
# while True:
#     element = input()
#     if element == 'stop':
#         break
#     quantity = int(input())
#     if element in book:
#         book[element] += quantity
#     else:
#         book[element] = quantity
# for el, q in book.items():
#     print(f'{el} -> {q}')

resources = {}
while True:
    current_resources = input()
    if current_resources == 'stop':
        break
    current_quantity = int(input())
    if current_resources not in resources: # ili not in resources.keys()
        resources[current_resources] = 0
    resources[current_resources] += current_quantity
for resource, quantity in resources.items():
    print(f'{resource} -> {quantity}')

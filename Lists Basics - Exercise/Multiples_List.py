factor = int(input())
count = int(input())
multiples_list = []

for number in range(1, 10000):
    if number % factor == 0:
        multiples_list.append(number)
        if len(multiples_list) < count:
            continue
        else:
            break
print(multiples_list)

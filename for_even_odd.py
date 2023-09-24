x = int(input())
for i in range(x):
    y = int(input())
    if y % 2 != 0:
        print(f'{y} is odd!')
        exit()
print('All numbers are even.')

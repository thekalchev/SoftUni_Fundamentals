string = input().split(', ')
for num in string:
    if num == '0':
        string.remove(num)
        string.append(num)
int_list = list(map(int, string))
print(int_list)
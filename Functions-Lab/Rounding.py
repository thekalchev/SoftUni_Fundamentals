string_list = input().split()
list_with_integers = []
for num in string_list:
    list_with_integers.append(round(float(num)))
print(list_with_integers)
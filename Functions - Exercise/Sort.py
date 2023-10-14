sequence= input().split()
list_of_strings = list(sorted(sequence))
list_of_integers = []
for i in list_of_strings:
    num = int(i)
    list_of_integers.append(num)
print(sorted(list_of_integers))


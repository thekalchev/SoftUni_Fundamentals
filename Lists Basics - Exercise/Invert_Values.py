string_of_numbers = input()
list_of_strings = string_of_numbers.split(' ')
list_as_integers = []
for num in list_of_strings:
    new_num = int(num)  #moje vmesto da go umnojavame po -1 da zapishem -int
    list_as_integers.append(new_num * -1) #reversing the value
print(list_as_integers)

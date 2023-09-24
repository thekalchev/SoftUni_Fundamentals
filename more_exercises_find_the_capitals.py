# input_string = input()
#
# capitals = [index for index, char in enumerate(input_string) if char.isupper()]
#
# print(capitals)

word = input()
capitals = []
for index, char in enumerate(word):
    if char.isupper():
        capitals.append(index)
print(capitals)

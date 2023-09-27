number = int(input())
word = input()
old_list = []
new_list = []
for _ in range(number):
    string = input()
    old_list.append(string)
    if word in string:
        new_list.append(string)
print(old_list)
print(new_list)
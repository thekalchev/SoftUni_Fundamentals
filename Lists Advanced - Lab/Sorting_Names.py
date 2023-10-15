names = input().split(', ')
sorted_names_by_length = sorted(names, key=lambda x: (-len(x), x))
print(sorted_names_by_length)

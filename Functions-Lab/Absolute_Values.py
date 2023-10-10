nums_list = input().split()
absolute_value = []
for num in nums_list:
    absolute_value.append(abs(float(num)))
print(absolute_value)

#list comprehension way:
# nums_list = input().split()
# absolute_values = [abs(float(num)) for num in nums_list]
# print(absolute_values)
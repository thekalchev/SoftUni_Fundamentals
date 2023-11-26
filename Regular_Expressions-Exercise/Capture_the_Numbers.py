import re
text = input()
pattern = '\d+(?!w+)'
result = re.findall(pattern, text)
for match in result:
    print(match)
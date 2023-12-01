import re

text = input()
pattern = r'(#|@)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'
matches = {}
result = re.findall(pattern, text)
for word in result:
    if word[1] == word[2][::-1]:
        matches[word[1]] = word[2]

if len(result) > 0:
    print(f'{len(result)} word pairs found!')
if len(result) == 0:
    print('No word pairs found!')
if len(matches) == 0:
    print(f'No mirror words!')
if len(matches) > 0:
    print(f'The mirror words are:')
    print(", ".join([f"{pair} <=> {pair[::-1]}" for pair in matches]))


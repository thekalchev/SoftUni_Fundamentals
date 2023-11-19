import re

phone_nums = input()
valid_phone_nums = []
pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
result = re.findall(pattern, phone_nums)
print(', '.join(result))

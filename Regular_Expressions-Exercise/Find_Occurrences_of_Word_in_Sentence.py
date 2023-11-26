import re

sentence = input()
word = input()
pattern = fr'(?i)\b{word}\b'  # (?i) means IGNORECASE
result = re.findall(pattern, sentence)
print(len(result))
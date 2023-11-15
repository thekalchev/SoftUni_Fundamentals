text = input()
digits = ''
letters = ''
special_characters = ''
for ch in text:
    if ch.isalpha():
        letters += ch
    elif ch.isdigit():
        digits += ch
    else:
        special_characters += ch
print(digits)
print(letters)
print(special_characters)

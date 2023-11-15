text = input()
encrypted_text = ''
for i in text:
    new_char = chr(ord(i) + 3)
    encrypted_text += new_char

print(encrypted_text)
message = input()
encrypted_message = ''
for i in message:
    new_char = chr(ord(i) + 3)
    encrypted_message += new_char
print(encrypted_message)

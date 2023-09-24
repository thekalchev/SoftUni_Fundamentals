key = int(input())
num_of_lines = int(input())
message = []
new_message = []
for line in range(num_of_lines):
    letter = input()
    message.append(ord(letter) + key)
for i in range(len(message)):
    new_message.append(chr(message[i]))
print(''.join(new_message))

# key = int(input())
# num_of_lines = int(input())
# decrypted_message = ""
# for current_line in range(num_of_lines):
#     line = input()
#     for char in line:
#         decrypted_char = chr(ord(char) + key)
#         decrypted_message += decrypted_char
# print(decrypted_message)

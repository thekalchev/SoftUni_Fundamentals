numbers = input().split()
text = list(input())
index = 0
message = ''
for number in numbers:
    digits_sum = sum(int(digit) for digit in number)
    char_index = digits_sum % len(text)
    message += text[char_index]
    text.pop(char_index)
print(message)



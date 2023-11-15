text = input()
emoji = ''
for i in range(len(text)):
    if text[i] == ':':
        emoji += text[i] + text[i+1]
        print(emoji)
        emoji = ''

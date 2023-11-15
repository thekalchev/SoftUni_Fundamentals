text = input()
new_text = ''
for i in range(len(text)):
    if i != len(text) - 1:
        if text[i] == text[i + 1]:
            new_text += ''
        else:
            new_text += text[i]
    else:
        new_text += text[i]
print(new_text)

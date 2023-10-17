secret_message = input().split()
for word in secret_message:
    letter_string = []
    word = list(word)
    for char in word:
        if char.isnumeric():
            letter_string.append(char)
    letter_ascii = chr(int(''.join(letter_string)))
    for char in word:
        if char.isnumeric():
            word.remove(char)
    word[1], word[-1] = word[-1], word[1]
    word[0] = letter_ascii
    final_word = ''.join(word)
    print(final_word, end=' ')

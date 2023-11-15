# dict_with_words = {}
# while True:
#     word = input()
#     if word == 'end':
#         break
#     reversed_word = word[::-1]
#     dict_with_words[word] = reversed_word
#
# for word, reversed_word in dict_with_words.items():
#     print(f'{word} = {reversed_word}')


# text = input()
# while text != 'end':
#     text_reversed = ''
#     for ch in reversed(text):
#         text_reversed += ch
#     print(f'{text} = {text_reversed}')
#     text = input()

while True:
    word = input()
    if word == 'end':
        break
    reversed_word = word[::-1]
    print(f'{word} = {reversed_word}')
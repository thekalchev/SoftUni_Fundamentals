# banned_words = input().split(', ')
# text = input()
# for word in banned_words:
#     while word in text:
#         text = text.replace(word, '*' * len(word))
# print(text)

name = ('Mario')
n = list(name)
n[0] = 'B'
print(''.join(n))
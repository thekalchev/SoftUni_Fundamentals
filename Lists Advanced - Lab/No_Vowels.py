# vowels = ['a', 'e', 'o', 'i', 'y', 'Y', 'u', 'A', 'E', 'O', 'I', 'U']
# original_word = input()
# word_without_vowels = [char for char in original_word if char not in vowels]
# print(''.join(word_without_vowels))

text = input()
sorted_text = [char for char in text if char.lower() not in ['a', 'e', 'o', 'i', 'y', 'u']]
print(''.join(sorted_text))
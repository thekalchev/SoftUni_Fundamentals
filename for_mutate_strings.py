word1 = input()
word2 = input()
last_printed_word = word1

for i in range(len(word1)):
    left_part = word2[:i + 1]
    right_part = word1[i + 1:]
    new_word = left_part + right_part
    if new_word == last_printed_word:
        continue
    print(new_word)
    last_printed_word = new_word
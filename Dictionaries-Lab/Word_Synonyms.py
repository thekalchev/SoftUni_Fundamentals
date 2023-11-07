count_of_words = int(input())
synonyms = {}
for word in range(count_of_words):
    current_word = input()
    synonym = input()

    if current_word in synonyms:
        synonyms[current_word].append(synonym)
    else:
        synonyms[current_word] = [synonym]

for word, synonym_list in synonyms.items():
    synonym_string = ', '.join(synonym_list)
    print(f'{word} - {synonym_string}')
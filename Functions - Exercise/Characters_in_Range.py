# def characters_between_chars(char1, char2):
#     chars_between = []
#     for char in range(ord(char1) + 1, ord(char2)):
#         chars_between.append(chr(char))
#     return ' '.join(chars_between)
#
#
# char1 = input()
# char2 = input()
#
# result = characters_between_chars(char1, char2)
# print(result)


def all_the_characters(first_char: str, second_char: str):
    characters = []
    for current_character_as_digit in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(current_character_as_digit))
    return characters

first_character = input()
second_character = input()
final_result = all_the_characters(first_character, second_character)
print(' '.join(final_result)) #join raboti samo sys stringove

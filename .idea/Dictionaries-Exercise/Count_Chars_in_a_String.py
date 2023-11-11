# input_string = input()
# input_string = input_string.replace(" ", "")
# char_count = {}
# for char in input_string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
#
# for char, count in char_count.items():
#     print(f"{char} -> {count}")

symbols = [character for character in input() if character != ' ']
letters = {}
for symbol in symbols:
    if symbol not in letters:
        letters[symbol] = 0
    letters[symbol] += 1
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")

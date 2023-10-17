# sequence1 = input().split(', ')
# sequence2 = input().split(', ')
# substrings = []
# for word1 in sequence1:
#     for word2 in sequence2:
#         if word1 in word2:
#             substrings.append(word1)
#             break
# print(substrings)

sequence1 = input().split(', ')
sequence2 = input().split(', ')
print([first_string for first_string in sequence1 if any(first_string in second_string for second_string in sequence2)])
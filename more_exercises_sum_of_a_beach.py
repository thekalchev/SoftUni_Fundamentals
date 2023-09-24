gibberish = input().lower()
total_count = 0
target_words = ["sand", "water", "fish", "sun"]

for word in target_words:
    count = gibberish.count(word)
    total_count += count
print(total_count)

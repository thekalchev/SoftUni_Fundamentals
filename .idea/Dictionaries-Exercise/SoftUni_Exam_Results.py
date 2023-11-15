submissions = {}
languages = {}

while True:
    data = input()
    if data == "exam finished":
        break

    if '-banned' in data:
        username, _ = data.split('-')
        submissions.pop(username, None)
        continue

    username, language, points = data.split('-')
    points = int(points)

    if username not in submissions:
        submissions[username] = {}

    if language not in submissions[username]:
        submissions[username][language] = points
    else:
        submissions[username][language] = max(submissions[username][language], points)

    if language not in languages:
        languages[language] = 1
    else:
        languages[language] += 1

print("Results:")
for user in submissions:
    max_points = max(submissions[user].values())
    print(f"{user} | {max_points}")

print("Submissions:")
for lang, count in languages.items():
    print(f"{lang} - {count}")

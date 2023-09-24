snowballs_count = int(input())
best_snowball = 0
best_weight = 0
best_time = 0
best_quality = 0
for snowball in range(snowballs_count):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > best_snowball:
        best_snowball = snowball_value
        best_weight = snowball_weight
        best_time = snowball_time
        best_quality = snowball_quality
        snowball_value = 0
print(f"{best_weight} : {best_time} = {int(best_snowball)} ({best_quality})")

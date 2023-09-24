actor_name = input()
academy_points = float(input())
judges_count = int(input())
total_points_without_starting = 0
for i in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    total_points_without_starting += ((judge_points * len(judge_name))/2)
    total_points = total_points_without_starting + academy_points
    if total_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        exit()
print(f'Sorry, {actor_name} you need {1250.5 - total_points :.1f} more!')


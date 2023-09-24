time_for_filming = int(input())
scenes_count = int(input())
scene_duration = int(input())

filming_preparation = time_for_filming * .15
scenes_time = scene_duration * scenes_count
total_time = filming_preparation + scenes_time
leftover_time = time_for_filming - total_time
if time_for_filming >= total_time:
    print(f'You managed to finish the movie on time! You have {leftover_time:.0f} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {leftover_time*-1:.0f} minutes.')

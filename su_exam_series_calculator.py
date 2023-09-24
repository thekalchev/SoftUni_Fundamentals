from math import floor
show_name = input()
seasons = int(input())
episodes = int(input()) #in every episode there's 20% ads more
episode_length = float(input()) #no ads
episode_with_ads = episode_length * 1.20
additional_time = seasons * 10
total_time = seasons * episodes * episode_with_ads + additional_time
print(f'Total time needed to watch the {show_name} series is {floor(total_time)} minutes.')


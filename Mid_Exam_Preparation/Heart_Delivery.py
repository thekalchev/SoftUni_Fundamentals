neighborhood = list(map(int, input().split('@')))
commands = input()
position = 0

while commands != "Love!":
    jump_length = int(commands.split()[1])
    position = (position + jump_length) % len(neighborhood)
    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")

    commands = input()

remaining_houses = len([house for house in neighborhood if house > 0])
print(f"Cupid's last position was {position}.")
if remaining_houses == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {remaining_houses} places.")

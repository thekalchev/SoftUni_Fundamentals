targets = list(map(int, input().split()))

while True:
    command = input()

    if command == "End":
        break

    index = int(command)

    if 0 <= index < len(targets) and targets[index] != -1:
        shot_value = targets[index]
        targets[index] = -1

        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > shot_value:
                    targets[i] -= shot_value
                else:
                    targets[i] += shot_value

shot_targets = [target for target in targets if target == -1]
print(f"Shot targets: {len(shot_targets)} -> {' '.join(map(str, targets))}")

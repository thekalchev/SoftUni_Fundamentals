initial_loot = input().split("|")
command = input()
treasure_chest = initial_loot

while command != "Yohoho!":
    command_data = command.split()
    action = command_data[0]

    if action == "Loot":
        items_to_add = command_data[1:]
        for item in items_to_add:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif action == "Drop":
        index = int(command_data[1])
        if 0 <= index < len(treasure_chest):
            item_to_drop = treasure_chest[index]
            treasure_chest.pop(index)
            treasure_chest.append(item_to_drop)

    elif action == "Steal":
        count = int(command_data[1])
        stolen_items = treasure_chest[-count:]
        treasure_chest = treasure_chest[:-count]
        print(", ".join(stolen_items))

    command = input()
    
if treasure_chest:
    average_gain = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")

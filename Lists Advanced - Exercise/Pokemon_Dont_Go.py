def modify_pokemon_distances(distances, index):
    if not distances:
        return 0

    removed_element = 0

    if index < 0:
        removed_element = distances.pop(0)
        distances.insert(0, distances[-1])
    elif index >= len(distances):
        removed_element = distances.pop()
        distances.append(distances[0])
    else:
        removed_element = distances.pop(index)

    for i in range(len(distances)):
        if distances[i] <= removed_element:
            distances[i] += removed_element
        else:
            distances[i] -= removed_element

    return removed_element

# Input: Initial sequence of distances
distances = list(map(int, input().split()))
removed_elements_sum = 0

while distances:
    index = int(input())
    removed_elements_sum += modify_pokemon_distances(distances, index)

# Output: Sum of removed elements
print(removed_elements_sum)

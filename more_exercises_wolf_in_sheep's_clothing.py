# Input
input_string = input()

# Split the input string into a list of animals
animals = input_string.split(", ")

# Find the position of the wolf
wolf_position = animals.index("wolf")

# Check if the wolf is the closest animal to you
if wolf_position == len(animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    sheep_number = len(animals) - wolf_position - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")

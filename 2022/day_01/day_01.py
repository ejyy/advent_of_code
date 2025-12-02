part1 = 0
part2 = 0

# Parse the input file
input = [line.split("\n") for line in open("day_01_input.txt", 'r').read().strip().split("\n\n")]

ranked_calories = []

for line in input:
    # Calculate the line's calorie sum and append to list
    line_calories = sum(list(map(int, line)))
    ranked_calories.append(line_calories)

# Sort descending
ranked_calories.sort(reverse = True)

# Part1 - elf carrying the maximum calories
part1 = ranked_calories[0]

# Part2 - total calories of top-3 elves
part2 = ranked_calories[0] + ranked_calories[1] + ranked_calories[2]

print("Part 1:", part1)
print("Part 2:", part2)

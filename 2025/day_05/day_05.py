part1 = 0
part2 = 0

# Parse the input file
input = [line.split("\n") for line in open("day_05_input.txt", 'r').read().strip().split("\n\n")]

# Convert the ranges to integer tuples (start, end)
ranges = [tuple(map(int, r.split("-"))) for r in input[0]]

# Convert the ingredient IDs to integers
ingredients = map(int, input[1])

# Part1 - count number of fresh ingredients
for i in ingredients:
    for r in ranges:
        # Check if ingredient ID is bound by the range
        # Initially tried set(); crashed immediately
        if i >= r[0] and i <= r[1]:
            part1 += 1
            break

# Part2 - number of IDs bounded by the overlapping ranges

print("Part 1:", part1)
print("Part 2:", part2)

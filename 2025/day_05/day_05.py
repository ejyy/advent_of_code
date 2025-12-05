part1 = 0
part2 = 0

# Parse the input file
input = [line.split("\n") for line in open("day_05_input.txt", 'r').read().strip().split("\n\n")]

# Convert the ranges to integer lists (start, end)
ranges = [list(map(int, r.split("-"))) for r in input[0]]

# Convert the ingredient IDs to integers
ingredients = map(int, input[1])

# Part1 - count number of fresh ingredients
for i in ingredients:
    for r in ranges:
        # Check if ingredient ID is bound by the range
        # Initially tried set(); crashed immediately
        if i >= r[0] and i <= r[1]:
            part1 += 1
            break # Prevent double counting if in multiple ranges

# Part2 - number of IDs bounded by the overlapping ranges
# Sort the ranges by start (ascending)
ranges.sort()

# Re-create ranges though with merged bounds where overlaps occur
merged_ranges = []

for start, end in ranges:
    last_entry = merged_ranges[-1] if merged_ranges else None
    # Check if start <= previous end
    if last_entry and start <= (last_entry[1] + 1):
        # Update the last entry end to the new end (if higher)
        last_entry[1] = max(last_entry[1], end)
    else:
        # Append the to list if no entries, or non-overlapping
        merged_ranges.append([start, end])

# Sum the bounds of the ranges (+1 fencepost error)
part2 = sum((end - start) + 1 for start, end in merged_ranges)

print("Part 1:", part1)
print("Part 2:", part2)

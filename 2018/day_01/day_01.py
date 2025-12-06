part1 = 0
part2 = 0

# Parse the input file, line by line
input = [int(line.strip().replace("+", "")) for line in open("day_01_input.txt", 'r')]

# Replace '+' symbol, convert to int and sum
part1 = sum(input)

# Keep a set of all reached numbers
reached = set()
current = 0

# Use cycle to make repeated passes through input
from itertools import cycle

pool = cycle(input)

# For repeated passes through input
for num in pool:
    # Update current position with new instruction
    current += num
    # If current position in set of reached values, break and provide answer
    if current in reached:
        part2 = current
        break
    # If not, add to the set
    else:
        reached.add(current)

print("Part 1:", part1)
print("Part 2:", part2)

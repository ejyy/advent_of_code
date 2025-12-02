part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_03_input.txt", 'r')]

import re

for line in input:
    # Use Regex to match 'plain mul'
    plain_mul_matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)

    # Perform the multiplication for each match
    for match in plain_mul_matches:
        part1 += int(match[0]) * int(match[1])

print("Part 1:", part1)
print("Part 2:", part2)

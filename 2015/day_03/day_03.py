part1 = 0
part2 = 0

# Parse the input file, line by line
input = [list(line.strip()) for line in open("day_03_input.txt", 'r')][0]

# Maintain sets of uniquely visited locations
uniques_p1 = set()
uniques_p2 = set()

# Dict of directions, mapping instruction to (x, y) coordinate deltas
directions = {
    "^": (0, 1),
    ">": (1, 0),
    "<": (-1, 0),
    "v": (0, -1)
}

# Starting location at 0,0 (ensure added to uniques)
location_p1 = (0, 0)
uniques_p1.add(location_p1)

# Part1 - loop through, adding new location to the uniques, then count total
for instruction in input:
    dx, dy = directions[instruction]
    new_x, new_y = location_p1[0] + dx, location_p1[1] + dy
    uniques_p1.add((new_x, new_y))
    location_p1 = (new_x, new_y)

part1 = len(uniques_p1)

# Starting location at 0,0 (ensure added to uniques)
location_santa = (0, 0)
location_robo = (0, 0)
uniques_p2.add(location_santa) # Both the same so only need to add once

# Part2 - loop through, adding new location (two movers) to the uniques, then count total
for idx, instruction in enumerate(input):
    dx, dy = directions[instruction]

    # Santa goes first (zero)
    if idx % 2 == 0:
        new_x, new_y = location_santa[0] + dx, location_santa[1] + dy
        uniques_p2.add((new_x, new_y))
        location_santa = (new_x, new_y)
    else:
        new_x, new_y = location_robo[0] + dx, location_robo[1] + dy
        uniques_p2.add((new_x, new_y))
        location_robo = (new_x, new_y)

part2 = len(uniques_p2)

print("Part 1:", part1)
print("Part 2:", part2)

part1 = 0
part2 = 0

# Parse the input file, line by line
input = [list(line.strip()) for line in open("day_06_input.txt", 'r')]

# Find starting point ("^")
for row_k, row_v in enumerate(input):
    # Process grid column by column
    for column_k, column_v in enumerate(row_v):
        if column_v == "^":
            current_position = (row_k, column_k)

# Direction reference (up, right, down, left)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_index = 0

while True:
    offset = directions[direction_index]
    new_x, new_y = current_position[0] + offset[0], current_position[1] + offset[1]

    # Out of grid bounds detection
    if new_x < 0 or new_x >= len(input) or new_y < 0 or new_y >= len(input[0]):
        break

    # Collision detection
    if input[new_x][new_y] == "#":
        direction_index = (direction_index + 1) % 4
    else:
        # Mark as visited
        input[current_position[0]][current_position[1]] = "X"

        # Move pointer to new current position
        input[new_x][new_y] = "^"
        current_position = (new_x, new_y)

# Part1 - sum of distinct visited positions
part1 = sum(input, []).count("X")+1

print("Part 1:", part1)
print("Part 2:", part2)

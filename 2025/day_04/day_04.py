part1 = 0
part2 = 0

# Parse the input file, line by line
input = [list(line.strip()) for line in open("day_04_input.txt", 'r')]

# Direction matrix (row, column) -> L, UL, A, UR, R, LR, B, LL
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def count_adjacents(grid, row, column):
    count = 0
    # Check adjacent 8 cells to enquire about contents
    for d_row, d_column in directions:
        # Propose a new grid reference based on current position adjusted by direction
        new_row, new_column = row + d_row, column + d_column

        # Bounds checking to ensure not off-grid
        if new_row < 0 or new_row >= len(grid) or new_column < 0 or new_column >= len(grid[0]):
            continue

        # Check if proposed grid reference contains a roll, increment if so
        if grid[new_row][new_column] == "@":
            count += 1

    return count

first_pass = True

while True:
    to_remove = []

    # Process grid row by row
    for row_k, row_v in enumerate(input):
        # Process grid column by column
        for column_k, column_v in enumerate(row_v):
            # Only interested in rolls
            if column_v != "@":
                continue

            # Append to list of rolls to remove if <4 adjacents
            if count_adjacents(input, row_k, column_k) < 4:
                to_remove.append((row_k, column_k))

    # Part1 - First pass of the loop is number to remove for part1
    if first_pass:
        part1 = len(to_remove)
        first_pass = False

    # If nothing to remove, stop iterating
    if not to_remove:
        break

    # Part2 - remove the rolls that can be each round, and increment
    for row, column in to_remove:
        input[row][column] = "."
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)

part1 = 0
part2 = 0

# Parse the input file, line by line
input = [list(line.strip()) for line in open("day_04_input.txt", 'r')]

# Direction matrix (row, column) -> L, UL, A, UR, R, LR, B, LL
directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

# Process grid row by row
for row_k, row_v in enumerate(input):
    # Process grid column by column
    for column_k, column_v in enumerate(row_v):
        # Check adjacent 8 cells to enquire about contents
        adjacents = []
        for direction in directions:
            # Propose a new grid reference based on current position adjusted by direction
            new_row, new_column = row_k + direction[0], column_k + direction[1]

            # Bounds checking to ensure not off-grid
            if new_row < 0 or new_row >= len(input) or new_column < 0 or new_column >= len(row_v):
                continue

            # Check if proposed grid reference contains a roll, append to list if so
            if input[new_row][new_column] == "@":
                adjacents.append((new_row, new_column))

        # Part1 - If current cell is a roll and it has less than 4 adjacents, increment
        if column_v == "@" and len(adjacents) < 4:
            part1 += 1

print("Part 1:", part1)
print("Part 2:", part2)

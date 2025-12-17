part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_02_input.txt", 'r')]

# Direction reference
moves = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

# Part 1 keypad layout
keypad_part1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Part 2 keypad layout (using 0 for 'padding')
keypad_part2 = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, "A", "B", "C", 0],
    [0, 0, "D", 0, 0]
]

# Current starting position (row, col) is 5
row, col = 1, 1

# List of appended codes
code_part1 = []

for line in input:
    for instruction in line:
        dr, dc = moves[instruction]
        new_row = row + dr
        new_col = col + dc

        # Only move if still on keypad (bounds checking based on list length)
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            row, col = new_row, new_col

    # Press the button
    code_part1.append(str(keypad_part1[row][col]))

part1 = "".join(code_part1)

# Reset current starting position (row, col) to 5 (but different)
row, col = 2, 0

# List of appended codes
code_part2 = []

for line in input:
    for instruction in line:
        dr, dc = moves[instruction]
        new_row = row + dr
        new_col = col + dc

        # Only move if still on keypad (bounds checking based on list length and 'padding')
        if (0 <= new_row < 5 and 0 <= new_col < 5) and (keypad_part2[new_row][new_col] != 0):
            row, col = new_row, new_col

    # Press the button
    code_part2.append(str(keypad_part2[row][col]))

part2 = "".join(code_part2)

print("Part 1:", part1)
print("Part 2:", part2)

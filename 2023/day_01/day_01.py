part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_01_input.txt", 'r')]

for line in input:
    # Extract the numbers in the line, keeping as a string for easy merging
    all_numbers = [n for n in list(line) if n.isdigit()]

    # Merge the first and last number to obtain the line's calibration value
    calibration_value = all_numbers[0] + all_numbers[-1]

    # Part1 - sum of calibration values
    part1 += int(calibration_value)

print("Part 1:", part1)
print("Part 2:", part2)

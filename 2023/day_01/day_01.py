part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_01_input.txt", 'r')]

# Numbers as text
text_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in input:
    # Extract the numbers in the line, keeping as a string for easy merging
    all_digits = [n for n in list(line) if n.isdigit()]

    # Extract the numbers in the line, from text form
    all_text_nums = [num for num in text_nums if num in line]
    # TODO: But they need to be matched together, respecting order

    # Part1 - sum of digit calibration values
    digit_calibration_value = all_digits[0] + all_digits[-1]
    part1 += int(digit_calibration_value)

print("Part 1:", part1)
print("Part 2:", part2)

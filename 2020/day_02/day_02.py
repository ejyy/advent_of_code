part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_02_input.txt", 'r')]

for line in input:
    # Split initially on whitespace
    whitespace_split = line.split(" ")

    # Extract the range of repetitions, as integer
    low_num, high_num = map(int, whitespace_split[0].split("-"))

    # Extract the test string and target letter
    letter = whitespace_split[1][:-1]
    test_string = whitespace_split[2]

    # Count number of occurences of letter in test string and increment accordingly
    actual_occurences = test_string.count(letter)
    if low_num <= actual_occurences <= high_num:
        part1 += 1

    # Extract the letter at the position (note not zero indexing)
    letter_at_low_num = test_string[low_num - 1]
    letter_at_high_num = test_string[high_num - 1]

    # Check positioning valid and increment accordingly
    if (letter_at_low_num == letter) != (letter_at_high_num == letter):
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)

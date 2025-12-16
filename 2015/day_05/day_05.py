part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_05_input.txt", 'r')]

def check_nice(string):
    vowel_count = 0
    double_count = 0
    bad_strings = 0

    for x, y in zip(string, string[1:]):
        if x == y:
            double_count += 1
        if str(x + y) in ["ab", "cd", "pq", "xy"]:
            bad_strings += 1

    for idx, char in enumerate(string):
        if char in ["a", "e", "i", "o", "u"]:
            vowel_count += 1

    if (vowel_count >= 3) and (double_count >= 1) and (bad_strings < 1):
        return True
    else:
        return False

for line in input:
    if check_nice(line):
        part1 += 1

print("Part 1:", part1)
print("Part 2:", part2)

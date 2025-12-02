part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_02_input.txt", 'r')]

for line in input:
    # Extract each number in the row as an integer
    report = [int(x) for x in line.split()]
    report_safe = True

    # Check if every number increasing or decreasing per row
    increasing = all(report[i+1] - report[i] > 0 for i in range(len(report)-1))
    decreasing = all(report[i+1] - report[i] < 0 for i in range(len(report)-1))

    if not (increasing or decreasing):
        report_safe = False

    # Check if difference conditions met
    for i in range(len(report)-1):
        diff = abs(report[i+1] - report[i])
        if diff < 1 or diff > 3:
            report_safe = False

    if report_safe:
        part1 += 1

print("Part 1:", part1)
print("Part 2:", part2)

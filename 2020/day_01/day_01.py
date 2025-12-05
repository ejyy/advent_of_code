part1 = 0
part2 = 0

# Parse the input file, line by line
input = [int(line.strip()) for line in open("day_01_input.txt", 'r')]

for l1 in input:
    for l2 in input:
        if l1 == l2:
            continue
        if l1 + l2 == 2020:
            part1 = l1 * l2
            break

for l1 in input:
    for l2 in input:
        for l3 in input:
            if l1 == l2 or l1 == l3 or l2 == l3:
                continue
            if l1 + l2 + l3 == 2020:
                part2 = l1 * l2 * l3
                break

print("Part 1:", part1)
print("Part 2:", part2)

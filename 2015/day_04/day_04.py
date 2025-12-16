part1 = 0
part2 = 0

# Parse the input file
input = [line.strip() for line in open("day_04_input.txt", 'r')]

import hashlib

increment_part1 = 0

# Loop through, calculating MD5 until correct increment found
while True:
    md5_input = str(input[0]) + str(increment_part1)
    res = hashlib.md5(md5_input.encode()).hexdigest()
    if res.startswith("00000"):
        part1 = increment_part1
        break
    increment_part1 += 1

increment_part2 = 0

# Loop through, calculating MD5 until correct increment found
while True:
    md5_input = str(input[0]) + str(increment_part2)
    res = hashlib.md5(md5_input.encode()).hexdigest()
    if res.startswith("000000"):
        part2 = increment_part2
        break
    increment_part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)

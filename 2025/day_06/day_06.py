part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip().split() for line in open("day_06_test.txt", 'r')]

import numpy as np
import math

# Process all integers (excluding symbols) into numpy array
input_np = np.asarray(input[:-1], dtype='int64')

# Transpose the numpy
input_np = np.transpose(input_np)

# Loop through the symbols
for idx, symbol in enumerate(input[-1]):
    # If symbol '+', perform sum
    if symbol == "+":
        part1 += sum(list(input_np[idx]))
    # If symbol '*', multiply out
    if symbol == "*":
        part1 += math.prod(list(input_np[idx]))

# Part 2 needs to be completely recalculated, as stripped whitespace in part 1

print("Part 1:", part1)
print("Part 2:", part2)

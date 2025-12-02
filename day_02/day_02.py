part1 = 0
part2 = 0

# Parse the input file, line by line
input = [line.strip() for line in open("day_02_input.txt", 'r')]

for line in input:
    # Separate at every comma (",")
    split_line = line.split(",")

    for product_range in split_line:
        # Separate at every dash ("-")
        split_range = product_range.split("-")

        # Generate all numbers between the range
        full_product_range = range(int(split_range[0]), int(split_range[1])+1)

        for n in full_product_range:
            # To check if repetitive, split the number in half
            n = str(n)
            n_first_half, n_second_half = n[:len(n)//2], n[len(n)//2:]

            if n_first_half == n_second_half:
                part1 += int(n)

print("Part 1:", part1)
print("Part 2:", part2)

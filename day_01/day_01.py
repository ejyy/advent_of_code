def dial(initial_idx, rotation, dial_range=100):
    direction = str(rotation[0])
    delta_value = int(rotation[1:])
    delta = -delta_value if direction == "L" else delta_value

    total_delta = initial_idx + delta

    next_index = total_delta % dial_range

    crosses_zero = abs(total_delta // dial_range)

    return next_index, crosses_zero

with open("day_01_input.txt") as file:
    times_rest_on_zero = 0
    times_crosses_zero = 0

    starting_idx = 50

    for line in file:
        starting_idx, crosses_zero = dial(starting_idx, line.strip())

        if starting_idx == 0:
            times_rest_on_zero += 1

        times_crosses_zero += crosses_zero

print("Part 1:", times_rest_on_zero)
print("Part 2:", times_crosses_zero)

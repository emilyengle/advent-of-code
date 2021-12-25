def get_input():
    f = open("input.txt")
    positions = f.readline().strip().split(",")
    f.close()
    nums = [int(p) for p in positions]
    nums.sort()
    return nums


def get_median_positions(positions):
    if len(positions) % 2 == 1:
        return [positions[len(positions) / 2]]
    else:
        pos_1 = positions[len(positions) / 2 - 1]
        pos_2 = positions[len(positions) / 2]
        return [i for i in range(pos_1, pos_2 + 1)]


def get_average_positions(positions):
    return [sum(positions) / len(positions), sum(positions) / len(positions) + 1]


def get_constant_fuel_cost(positions, median):
    return sum(list(map(lambda p: abs(p - median), positions)))


def get_linear_fuel_cost(positions, average):
    """
    1 -> 1
    2 -> 3
    3 -> 6
    4 -> 10
    5 -> 15
    6 -> 21
    7 -> 28
    8 -> 36
    """
    initial_costs = list(map(lambda p: abs(p - average), positions))
    linear_costs = []
    for c in initial_costs:
        if c % 2 == 0:
            linear_costs.append((c + 1) * (c / 2))
        else:
            linear_costs.append((c + 1) * (c / 2) + (c / 2 + 1))
    return sum(linear_costs)


if __name__ == "__main__":
    positions = get_input()

    # Part 1
    medians = get_median_positions(positions)

    min_fuel_cost = None
    best_median = None
    for median in medians:
        fuel_cost = get_constant_fuel_cost(positions, median)
        if min_fuel_cost is None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            best_median = median

    print(best_median, min_fuel_cost)

    # Part 2
    averages = get_average_positions(positions)

    min_fuel_cost = None
    best_average = None
    for average in averages:
        fuel_cost = get_linear_fuel_cost(positions, average)
        if min_fuel_cost is None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            best_average = average

    print(best_average, min_fuel_cost)

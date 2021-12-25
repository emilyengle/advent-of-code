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


def get_fuel_cost(positions, median):
    return sum(list(map(lambda p: abs(p - median), positions)))


if __name__ == "__main__":
    positions = get_input()
    medians = get_median_positions(positions)

    min_fuel_cost = None
    best_median = None
    for median in medians:
        fuel_cost = get_fuel_cost(positions, median)
        if min_fuel_cost is None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            best_median = median

    print(best_median, min_fuel_cost)

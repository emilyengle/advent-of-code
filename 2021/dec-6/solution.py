def get_input():
    f = open("input.txt")
    initial_pop = f.readline().strip().split(",")
    f.close()
    return [int(p) for p in initial_pop]


def get_next_pop(prev_pop):
    next_pop = []
    num_new = 0
    for fish in prev_pop:
        if fish == 0:
            next_pop.append(6)
            num_new += 1
        else:
            next_pop.append(fish - 1)

    new_fish = [8 for _ in range(num_new)]
    next_pop.extend(new_fish)
    return next_pop


if __name__ == "__main__":
    prev_pop = get_input()

    for i in range(256):
        next_pop = get_next_pop(prev_pop)
        print("Day " + str(i) + " Num fish: " + str(len(next_pop)))
        prev_pop = next_pop

    print(len(prev_pop))

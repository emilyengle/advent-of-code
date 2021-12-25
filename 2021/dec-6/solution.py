def get_input():
    f = open("input.txt")
    initial_pop = f.readline().strip().split(",")
    f.close()
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for p in initial_pop:
        counts[int(p)] += 1
    return counts


def get_next_counts(counts):
    num_new = counts.pop(0)
    counts[6] += num_new
    counts.append(num_new)
    return counts


if __name__ == "__main__":
    counts = get_input()

    for i in range(256):
        next_counts = get_next_counts(counts)
        print(
            "Day "
            + str(i + 1)
            + " Population: "
            + str(next_counts)
            + " Num fish: "
            + str(sum(next_counts))
        )
        counts = next_counts

    print(sum(counts))

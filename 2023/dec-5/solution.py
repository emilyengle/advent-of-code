def convert(seeds, lines, i):
    ranges, num_lines, line = [], 0, lines[i]
    while line and (num_lines + i) < len(lines):
        ranges.append([int(n) for n in line.split(" ")])
        num_lines += 1
        if i + num_lines >= len(lines):
            break
        line = lines[i + num_lines]

    conversions = []
    for seed in seeds:
        seed_conversion = seed
        for dest, src, rng in ranges:
            if src <= seed < src + rng:
                seed_conversion = dest + (seed - src)
        conversions.append(seed_conversion)
    return conversions, ranges, num_lines


def convert_loc_to_seed(conversions, l):
    loc = l
    for c in range(len(conversions) - 1, -1, -1):
        conversion = conversions[c]
        for dest, src, rng in conversion:
            if dest <= loc < dest + rng:
                loc = src + (loc - dest)
                break
    return loc


def is_seed(ranges, s):
    for i in range(0, len(ranges), 2):
        start_seed, length = ranges[i], ranges[i + 1]
        if start_seed <= s < start_seed + length:
            return True

    return False


if __name__ == "__main__":
    orig_seeds = []
    seeds = []
    conversions = []
    lines = [line.strip() for line in open("input.txt").readlines()]

    for i in range(len(lines)):
        line = lines[i]

        if not line:
            i += 1
        elif line.startswith("seeds:"):
            orig_seeds = [int(s) for s in line.split("seeds: ")[1].split(" ")]
            seeds = orig_seeds.copy()
        elif "map" in line:
            seeds, conversion, num_lines = convert(seeds, lines, i + 1)
            conversions.append(conversion)
            i += num_lines

    # Part 1
    print(min(seeds))

    # Part 2
    loc = 0
    while True:
        s = convert_loc_to_seed(conversions, loc)
        if is_seed(orig_seeds, s):
            print(f"Smallest loc: {loc} from seed {s}")
            break
        loc += 1

def convert(seeds, lines, i):
    ranges, num_lines, line = [], 0, lines[i]
    while line and (num_lines + i) < len(lines) - 1:
        ranges.append([int(n) for n in line.split(" ")])
        num_lines += 1
        line = lines[i + num_lines]

    conversions = []
    for seed in seeds:
        seed_conversion = seed
        for dest, src, rng in ranges:
            if src <= seed < src + rng:
                seed_conversion = dest + (seed - src)
        conversions.append(seed_conversion)
    return conversions, num_lines


if __name__ == "__main__":
    seeds = []
    lines = [line.strip() for line in open("input.txt").readlines()]

    for i in range(len(lines)):
        line = lines[i]

        if not line:
            i += 1
        elif line.startswith("seeds:"):
            seeds = [int(s) for s in line.split("seeds: ")[1].split(" ")]
        elif "map" in line:
            seeds, num_lines = convert(seeds, lines, i + 1)
            i += num_lines

    print(min(seeds))

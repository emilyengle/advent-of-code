import math

lines = [line.strip() for line in open("input.txt").readlines()]
seq = [c for c in lines[0]]

map = {}
for i in range(2, len(lines)):
    key, left_right = lines[i].split(" = ")
    left, right = left_right[1 : len(left_right) - 1].split(", ")
    map[key] = {"L": left, "R": right}

# Part 1
num_steps, next_step, next_direction = 0, "AAA", seq[0]
while next_step != "ZZZ":
    next_direction = seq[num_steps % len(seq)]

    num_steps += 1
    next_step = map[next_step].get(next_direction)

print(num_steps)


# Part 2
def all_cycles_found(cycles):
    return all([len(c) > 0 for c in cycles.values()])


starting_nodes = list(filter(lambda m: m.endswith("A"), map))
nodes = starting_nodes.copy()
cycles = {n: [] for n in nodes}

num_steps, next_direction = 0, seq[0]
while not all_cycles_found(cycles):
    next_direction = seq[num_steps % len(seq)]
    num_steps += 1
    nodes = [map[n].get(next_direction) for n in nodes]

    for i, n in enumerate(nodes):
        if n.endswith("Z"):
            cycles[starting_nodes[i]].append(num_steps)

multiples = [c[0] for c in cycles.values()]
print(math.lcm(*multiples))

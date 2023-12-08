lines = [line.strip() for line in open("input.txt").readlines()]
seq = [c for c in lines[0]]

map = {}
for i in range(2, len(lines)):
    key, left_right = lines[i].split(" = ")
    left, right = left_right[1 : len(left_right) - 1].split(", ")
    map[key] = {"L": left, "R": right}

num_steps, next_step, next_direction = 0, "AAA", seq[0]
while next_step != "ZZZ":
    next_direction = seq[num_steps % len(seq)]

    num_steps += 1
    next_step = map[next_step].get(next_direction)

print(num_steps)

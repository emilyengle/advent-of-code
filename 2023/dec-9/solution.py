sum = 0
for seq in open("input.txt").readlines():
    initial_seq = [int(s) for s in seq.strip().split(" ")]
    patterns = [initial_seq]
    next_seq = initial_seq
    while not all(n == 0 for n in next_seq):
        following_seq = [
            next_seq[i + 1] - next_seq[i] for i in range(len(next_seq) - 1)
        ]
        next_seq = following_seq
        patterns.append(following_seq)

    for i in range(len(patterns) - 1, -1, -1):
        pattern = patterns[i]
        if i == len(patterns) - 1:
            pattern.append(0)
        else:
            pattern.append(pattern[-1] + patterns[i + 1][-1])

    sum += patterns[0][-1]

print(sum)

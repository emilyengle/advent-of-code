f = open("input.txt")

counts = []
for line in f.readlines():
    digits = line.strip()
    for idx, digit in enumerate(digits):
        if len(counts) < idx + 1:
            counts.append({0: 0, 1: 0})

        digit = int(digit)
        counts[idx][digit] += 1

gamma_rate = "".join(["0" if c[0] > c[1] else "1" for c in counts])
epsilon_rate = "".join(["0" if c[0] < c[1] else "1" for c in counts])

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
f.close()

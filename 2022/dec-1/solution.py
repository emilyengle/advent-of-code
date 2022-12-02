f = open('input.txt', 'r')

elves = [0]
for line in f.readlines():
    if line == '\n':
        elves.append(0)
    else:
        elves[len(elves) - 1] += int(line)

print(max(elves))

sorted_elves = sorted(elves)
print(sum(sorted_elves[len(sorted_elves) - 3:]))
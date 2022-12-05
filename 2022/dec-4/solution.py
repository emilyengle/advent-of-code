f = open('input.txt')
pairs = [[[int(i) for i in l.split('-')] for l in line.strip().split(',')] for line in f.readlines()]

# Part 1
# num_contains = 0
# for pair in pairs:
#     elf1 = pair[0]
#     elf2 = pair[1]
#     if (elf2[1] >= elf1[1] and elf2[0] <= elf1[0]) or (elf1[1] >= elf2[1] and elf1[0] <= elf2[0]):
#         num_contains += 1
# print(num_contains)

# Part 2
num_overlaps = 0
for pair in pairs:
    elf1 = pair[0]
    elf2 = pair[1]
    if not ((elf1[0] < elf2[0] and elf1[1] < elf2[0]) or (elf1[0] > elf2[1] and elf1[1] > elf2[1])):
        num_overlaps += 1

print(num_overlaps)
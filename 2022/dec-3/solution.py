f = open('input.txt')

def get_priority(item):
    return ord(item) - (38 if item.isupper() else 96)

priority_sum = 0

# Part 1
# for line in f.readlines():
#     line = [c for c in line.strip()]
#     split_index = int(len(line) / 2)
#     first_compartment = set(line[0:split_index])
#     second_compartment = set(line[split_index:])

#     common_item = list(first_compartment.intersection(second_compartment))[0]
#     priority_sum += get_priority(common_item)

# Part 2
lines = [line.strip() for line in f.readlines()]
for i in range(0, len(lines), 3):
    elf1 = set([c for c in lines[i]])
    elf2 = set([c for c in lines[i + 1]])
    elf3 = set([c for c in lines[i + 2]])

    badge = list(elf1.intersection(elf2).intersection(elf3))[0]
    priority_sum += get_priority(badge)

print(priority_sum)
f = open('input.txt')

crates = []
instructions = []

reading_crate = True
for line in f.readlines():
    if line.strip() == '':
        reading_crate = False
        continue

    if reading_crate:
        column = 0
        for i in range(0, len(line), 4):
            chunk = line[i:i+4].strip()

            # Number at bottom of crates
            if len(chunk) == 1:
                continue

            if not len(crates) > column + 1:
                crates.append([])
            # Empty spot in column
            if len(chunk) == 0:
                column += 1
                continue
            new_crate = [chunk[1]]
            new_crate.extend(crates[column])
            crates[column] = new_crate

            column += 1
    else:
        # [quantity, start, end]
        instruction = line.strip().split(' ')
        instructions.append([int(instruction[1]), int(instruction[3]), int(instruction[5])])

for instruction in instructions:
    num_moves = instruction[0]
    start = instruction[1]
    end = instruction[2]

    # Part 1
    # for n in range(num_moves):
    #     item = crates[start - 1].pop()
    #     crates[end - 1].append(item)

    # Part 2
    crates_to_move = crates[start-1][len(crates[start-1]) - num_moves:]
    del crates[start-1][len(crates[start-1]) - num_moves:]
    crates[end-1].extend(crates_to_move)

result = ''
for column in crates:
    if len(column) > 0:
        result += column[-1]

print(result)

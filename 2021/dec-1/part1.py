with open("input.txt") as f:
    prev = None
    num_increasing = 0

    for line in f.readlines():
        line = int(line.strip())
        if prev is None:
            prev = line
            continue
        if line > prev:
            num_increasing += 1
        prev = line

    print(num_increasing)
f.close()

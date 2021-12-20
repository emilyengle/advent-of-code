f = open("input.txt")

horizontal = 0
depth = 0
for line in f.readlines():
    instruction, num = line.strip().split(" ")
    num = int(num)

    if instruction == "forward":
        horizontal += num
    elif instruction == "down":
        depth += num
    elif instruction == "up":
        depth -= num

print(horizontal * depth)
f.close()

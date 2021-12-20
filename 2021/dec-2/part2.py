f = open("input.txt")

horizontal = 0
depth = 0
aim = 0
for line in f.readlines():
    instruction, num = line.strip().split(" ")
    num = int(num)

    if instruction == "forward":
        horizontal += num
        depth += aim * num
    elif instruction == "down":
        aim += num
    elif instruction == "up":
        aim -= num

print(horizontal * depth)
f.close()

with open("input.txt") as f:
    data = [int(line.strip()) for line in f.readlines()]

    prev_sum = data[0] + data[1] + data[2]
    num_increasing = 0
    for i in range(1, len(data) - 2):
        sum = data[i] + data[i + 1] + data[i + 2]
        if sum > prev_sum:
            num_increasing += 1
        prev_sum = sum
    print(num_increasing)

f.close()

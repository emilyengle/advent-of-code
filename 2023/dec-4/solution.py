points = 0
for line in open("input.txt").readlines():
    winning_nums, your_nums = line.strip().split(" | ")
    winning_nums = [
        int(num.strip())
        for num in winning_nums.split(": ")[1].split(" ")
        if num.strip()
    ]
    your_nums = [int(num.strip()) for num in your_nums.split(" ") if num.strip()]

    count_wins = sum([1 for n in your_nums if n in winning_nums])
    points += pow(2, count_wins - 1) if count_wins > 0 else 0

print(points)

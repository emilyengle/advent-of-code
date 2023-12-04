def count_card_wins(winning_numbers, card_numbers):
    return sum(1 for n in card_numbers if n in winning_numbers)


def count_points(count_matching_numbers):
    return pow(2, count_matching_numbers - 1) if count_matching_numbers > 0 else 0


def count_cards_earned(card_id, win_map):
    additional_ids = [
        card_id + i + 1
        for i in range(win_map[card_id - 1])
        if card_id + i < len(win_map)
    ]
    if len(additional_ids) == 0:
        return 1

    return 1 + sum(count_cards_earned(id, win_map) for id in additional_ids)


points = 0
card_wins = []  # card --> int for count of winning numbers it has
for idx, line in enumerate(open("input.txt").readlines()):
    winning_nums, your_nums = line.strip().split(" | ")
    winning_nums = [
        int(num.strip())
        for num in winning_nums.split(": ")[1].split(" ")
        if num.strip()
    ]
    your_nums = [int(num.strip()) for num in your_nums.split(" ") if num.strip()]

    count_wins = count_card_wins(winning_nums, your_nums)

    card_wins.append(count_wins)
    points += count_points(count_wins)

# Part 1
print(points)

# Part 2
num_cards = sum(count_cards_earned(c, card_wins) for c in range(1, len(card_wins) + 1))
print(num_cards)

possibility = {"red": 12, "green": 13, "blue": 14}


def convert_round_to_color_dict(s):
    d = {}
    for color_and_number in s.strip().split(", "):
        num, color = color_and_number.split(" ")
        d[color] = int(num)
    return d


def is_round_possible(round):
    colors = convert_round_to_color_dict(round)
    return all(colors[c] <= possibility[c] for c in colors.keys())


id_sum = 0
for line in open("input.txt").readlines():
    game_id, rounds = line.strip().split(": ")
    is_game_possible = all(is_round_possible(round) for round in rounds.split("; "))

    id = int(game_id.split(" ")[1])
    id_sum += id if is_game_possible else 0

print(id_sum)

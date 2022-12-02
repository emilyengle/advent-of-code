def get_choice_score(my_choice):
    if my_choice == 'X':
        return 1
    elif my_choice == 'Y':
        return 2
    elif my_choice == 'Z':
        return 3

def get_outcome_score(opponent_choice, my_choice):
    opponent_wins = [('A', 'Z'), ('B', 'X'), ('C', 'Y')]
    draws = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]
    my_wins = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
    if (opponent_choice, my_choice) in opponent_wins:
        return 0
    elif (opponent_choice, my_choice) in draws:
        return 3
    elif (opponent_choice, my_choice) in my_wins:
        return 6

def get_outcome_score_from_result(result):
    if result == 'X':
        return 0
    elif result == 'Y':
        return 3
    elif result == 'Z':
        return 6

def get_choice_score_from_result(opponent_choice, result):
    choose_rock = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]
    choose_paper = [('A', 'Z'), ('B', 'Y'), ('C', 'X')]
    choose_scissors = [('A', 'X'), ('B', 'Z'), ('C', 'Y')]
    if (opponent_choice, result) in choose_rock:
        return 1
    elif (opponent_choice, result) in choose_paper:
        return 2
    elif (opponent_choice, result) in choose_scissors:
        return 3

f = open('input.txt')
score = 0
for line in f.readlines():
    # Part 1
    # opponent_choice, my_choice = line.strip().split(' ')
    # score += get_choice_score(my_choice)
    # score += get_outcome_score(opponent_choice, my_choice)

    # Part 2
    opponent_choice, result = line.strip().split(' ')
    score += get_outcome_score_from_result(result)
    score += get_choice_score_from_result(opponent_choice, result)

print(score)
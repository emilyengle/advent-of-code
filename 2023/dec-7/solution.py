from typing import List

import functools
import pytest

hands = {}
card_strength_part_1 = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_strength_part_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
hand_strength = [
    "five_kind",
    "four_kind",
    "full_house",
    "three_kind",
    "two_pair",
    "one_pair",
    "high_card",
]

def get_strength_with_jacks(cards: List[str]):
    jack_count = cards.count('J')
    plain_cards = list(filter(lambda c: c != 'J', cards))
    uniqs = list(set(cards))
    counts = [cards.count(u) for u in uniqs]

    if jack_count == 0:
        return get_strength(plain_cards)
    elif jack_count == 1:
        if len(uniqs) == 5:
            return "one_pair"
        if len(uniqs) == 4:
            return "three_kind"
        if len(uniqs) == 3:
            # 1122J, 1112J
            return "four_kind" if counts.count(3) == 1 else "full_house"
        if len(uniqs) == 2:
            return "five_kind"
    elif jack_count == 2:
        if len(uniqs) == 4:
            return "three_kind"
        if len(uniqs) == 3:
            return "four_kind"
        if len(uniqs) == 2:
            return "five_kind"
    elif jack_count == 3:
        if len(uniqs) == 2:
            return "five_kind"
        return "four_kind"
    elif jack_count == 4:
        return "five_kind"
    elif jack_count == 5:
        return "five_kind"

    raise f'Unknown strength {cards}'


def get_strength(cards: List[str]):
    uniqs = list(set(cards))
    counts = [cards.count(u) for u in uniqs]

    if len(cards) in counts:
        return "five_kind"
    elif len(uniqs) == 2:
        return "four_kind" if counts.count(len(cards) - 1) == 1 else "full_house"
    elif len(counts) == len(cards):
        return "high_card"
    elif 3 in counts:
        return "three_kind"
    elif counts.count(2) == 2:
        return "two_pair"
    elif counts.count(1) == 3 and counts.count(2) == 1:
        return "one_pair"
    else:
        raise f"Unknown strength {cards}"


def sort_hand(h1, h2):
    # Part 2
    card_strength = card_strength_part_2
    s1 = hand_strength.index(hands[h1].get("strength"))
    s2 = hand_strength.index(hands[h2].get("strength"))
    if s1 != s2:
        return 1 if s1 > s2 else -1

    for idx, c1 in enumerate(h1):
        c2 = h2[idx]
        s1, s2 = card_strength.index(c1), card_strength.index(c2)
        if s1 != s2:
            return 1 if s1 > s2 else -1

    raise f"Cannot sort {h1} and {h2}"


if __name__ == "__main__":
    for line in [line.strip().split(" ") for line in open("input.txt").readlines()]:
        hand, bid = line

        # Part 1
        # strength = get_strength([c for c in hand])
        # Part 2
        strength = get_strength_with_jacks([c for c in hand])

        hands[hand] = {
            "bid": int(bid),
            "strength": strength,
        }

    sorted_hands = sorted(hands, key=functools.cmp_to_key(sort_hand), reverse=True)
    winnings = sum(hands[h].get("bid") * (i + 1) for i, h in enumerate(sorted_hands))
    print(winnings)


@pytest.mark.parametrize(
    "input,expected",
    [
        (["5", "5", "5", "5", "5"], "five_kind"),
        (["4", "4", "3", "4", "4"], "four_kind"),
        (["4", "4", "3", "4", "3"], "full_house"),
        (["6", "4", "6", "6", "K"], "three_kind"),
        (["Q", "7", "3", "Q", "7"], "two_pair"),
        (["4", "6", "3", "4", "5"], "one_pair"),
        (["4", "6", "3", "2", "T"], "high_card"),
    ],
)
def test_get_strength(input, expected):
    assert get_strength(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ("66J6J", "five_kind"),
        ("T55J5", "four_kind"),
        ("KTJJT", "four_kind"),
        ("QQQJA", "four_kind"),
        ("J6767", "full_house"),
        ("2233J", "full_house"),
        ("JJ345", "three_kind"),
        ("AJJ94", "three_kind"),
        ("98J81", "three_kind"),
        ("32T3K", "one_pair"),
        ("67834", "high_card"),
    ],
)
def test_get_strength_with_jacks(input, expected):
    assert get_strength_with_jacks([i for i in input]) == expected

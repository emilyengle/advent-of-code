from typing import List

import functools
import pytest

hands = {}
card_strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
hand_strength = [
    "five_kind",
    "four_kind",
    "full_house",
    "three_kind",
    "two_pair",
    "one_pair",
    "high_card",
]


def get_strength(cards: List[str]):
    uniqs = list(set(cards))
    counts = [cards.count(u) for u in uniqs]

    if 5 in counts:
        return "five_kind"
    elif len(uniqs) == 2:
        return "four_kind" if counts.count(4) == 1 else "full_house"
    elif len(counts) == 5:
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
        hands[hand] = {
            "bid": int(bid),
            "strength": get_strength([c for c in hand]),
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

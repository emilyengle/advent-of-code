num_containing_2 = 0
num_containing_3 = 0
strings = []


def is_one_letter_off(s1, s2):
    one_off = False
    for idx, c in enumerate(s1):
        if c != s2[idx] and one_off:
            # Already encountered one mismatch, not one letter off
            return False
        elif c != s2[idx]:
            # One allowed mismatch
            one_off = True
    return one_off


for line in open("input.txt").readlines():
    letter_map = {}
    line = line.strip()
    for letter in line:
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1

    num_containing_2 += 1 if any(c == 2 for c in letter_map.values()) else 0
    num_containing_3 += 1 if any(c == 3 for c in letter_map.values()) else 0

    for s in strings:
        if is_one_letter_off(s, line):
            print(s)
            print(line)
            break

    strings.append(line)

print(num_containing_2 * num_containing_3)

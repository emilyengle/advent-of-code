# Part 1
calibration_values = []

for line in open("input.txt").readlines():
    idx, first_digit = 0, None
    while first_digit is None:
        if line[idx].isdigit():
            first_digit = line[idx]
        else:
            idx += 1

    idx, second_digit = len(line) - 1, None
    while second_digit is None:
        if line[idx].isdigit():
            second_digit = line[idx]
        else:
            idx -= 1

    calibration_values.append(int(f"{first_digit}{second_digit}"))
print(sum(calibration_values))

# Part 2
calibration_values = []
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def is_spelled_out_number(s, end=False):
    for number in numbers.keys():
        if (end and s.endswith(number)) or (not end and s.startswith(number)):
            return numbers[number]
    return None


for line in open("input.txt").readlines():
    idx, first_digit = 0, None
    while first_digit is None:
        if line[idx].isdigit():
            first_digit = line[idx]
            break

        spelled_out_number = is_spelled_out_number(line[idx:])
        if spelled_out_number is not None:
            first_digit = spelled_out_number
        else:
            idx += 1

    idx, second_digit = len(line) - 1, None
    while second_digit is None:
        if line[idx].isdigit():
            second_digit = line[idx]

        spelled_out_number = is_spelled_out_number(line[0 : idx + 1], end=True)
        if spelled_out_number is not None:
            second_digit = spelled_out_number
        else:
            idx -= 1

    calibration_values.append(int(f"{first_digit}{second_digit}"))
print(sum(calibration_values))

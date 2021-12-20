def get_counts(data, idx):
    count_zero = 0
    count_one = 0
    for d in data:
        if int(d[idx]) == 0:
            count_zero += 1
        else:
            count_one += 1
    return count_zero, count_one


if __name__ == "__main__":
    f = open("input.txt")
    data = [line.strip() for line in f.readlines()]

    oxygen_data = data
    co2_data = data

    idx = 0
    while len(oxygen_data) > 1:
        count_zero, count_one = get_counts(oxygen_data, idx)
        kept_digit = 0 if count_zero > count_one else 1
        oxygen_data = filter(lambda d: int(d[idx]) == kept_digit, oxygen_data)
        idx += 1
    oxygen_rating = oxygen_data[0]

    idx = 0
    while len(co2_data) > 1:
        count_zero, count_one = get_counts(co2_data, idx)
        kept_digit = 0 if count_zero <= count_one else 1
        co2_data = filter(lambda d: int(d[idx]) == kept_digit, co2_data)
        idx += 1
    co2_rating = co2_data[0]

    print(oxygen_rating, co2_rating)
    print(int(oxygen_rating, 2) * int(co2_rating, 2))
    f.close()

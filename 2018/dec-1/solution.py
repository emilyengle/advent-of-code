freqs = open("input.txt").readlines()
freq_list = [int(freq[1:] if freq[0] == "+" else -1 * int(freq[1:])) for freq in freqs]

print(sum(freq_list))

result = 0
idx = 0
freq_seen = {0: True}
while True:
    result += freq_list[idx % len(freq_list)]
    if result in freq_seen:
        print(f"Encountered {result} again.")
        break
    else:
        freq_seen[result] = True
        idx += 1

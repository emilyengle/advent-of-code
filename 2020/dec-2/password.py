file = open('input.txt', 'r')

# Part 1
# valid_passwords = 0
# for raw_line in file.readlines():
#     line = raw_line.strip()
#     [policy, password] = line.split(': ')
#     [bounds, letter] = policy.split(' ')
#     [min_number, max_number] = bounds.split('-')
#     min_num = int(min_number)
#     max_num = int(max_number) 
    
#     num_occurrences = password.count(letter)
#     if num_occurrences >= min_num and num_occurrences <= max_num:
#         valid_passwords += 1

# print(valid_passwords)

# Part 2
valid_passwords = 0
for raw_line in file.readlines():
    line = raw_line.strip()
    [policy, password] = line.split(': ')
    [indices, letter] = policy.split(' ')
    [index_a, index_b] = indices.split('-')
    a = int(index_a)
    b = int(index_b) 

    num_occurrences = 0
    if password[a-1] == letter:
        num_occurrences += 1
    if password[b-1] == letter:
        num_occurrences += 1
    
    if num_occurrences == 1:
        valid_passwords += 1

print(valid_passwords)

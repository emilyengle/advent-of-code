f = open('input.txt')

chars = [c for c in f.readline().strip()]

num_uniq = 14
index = num_uniq - 1
while index < len(chars):
    char_set = set([chars[index - i] for i in range(0, num_uniq)])
    if len(char_set) == num_uniq:
        print(index + 1)
        break
    index += 1
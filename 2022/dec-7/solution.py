def print_filesystem(f, offset = 0):
    offset_str = '\t' * offset
    print(f"{offset_str}Directory {f.name}, {len(f.contents)} entries")
    for entry in f.contents:
        if type(entry) == File:
            print(f"{offset_str}\t{entry.name}, {entry.size}")
        else:
            print_filesystem(entry, offset + 1)

class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.contents = []

    def add(self, entry):
        self.contents.append(entry)

    def get_directory(self, name):
        if name == self.name:
            return self
        filtered = list(filter(lambda f: f.name == name, self.contents))
        if len(filtered) == 0:
            print_filesystem(filesystem)
        return filtered[0]

    def get_size(self):
        sum = 0
        for entry in self.contents:
            if type(entry) == File:
                sum += entry.size
            else:
                sum += entry.get_size()
        return sum

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

filesystem = Directory(None, '/')

f = open('input.txt')
lines = [l.strip() for l in f.readlines()]

i = 0
while i < len(lines):
    command = lines[i][2:]
    if command[0:2] == 'cd':
        command = command[3:]
        if command == '..':
            print(f'Before up: {filesystem.name}')
            filesystem = filesystem.parent
            print(f'After up: {filesystem.name}')
        else:
            filesystem = filesystem.get_directory(command)
        i += 1
    else: # ls
        i += 1
        next_line = lines[i]
        while next_line[0] != '$' and i < len(lines):
            parts = next_line.split(' ')
            if parts[0] == 'dir':
                filesystem.add(Directory(filesystem, parts[1]))
            else:
                filesystem.add(File(parts[1], int(parts[0])))
            i += 1
            if i < len(lines):
                next_line = lines[i]

while filesystem.parent is not None:
    filesystem = filesystem.parent

print_filesystem(filesystem)

def sum_directory_sizes(f, sum = 0, limit = 100000):
    f_size = f.get_size()
    total_sum = sum + f_size if f_size <= limit else sum

    for entry in f.contents:
        if type(entry) == Directory:
            total_sum += sum_directory_sizes(entry, sum)

    return total_sum

print(sum_directory_sizes(filesystem))

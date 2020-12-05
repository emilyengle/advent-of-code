def get_tree_map():
    map = []
    file = open('input.txt', 'r')
    for line in file.readlines():
        map.append(list(line.strip()))
    return map

def count_trees(tree_map, slope):
    count = 0
    coordinates = (0,0)
    while coordinates[0] < len(tree_map):
        value = tree_map[coordinates[0]][coordinates[1]]
        if is_tree(value):
            count += 1
        coordinates = get_next_coordinates(tree_map, coordinates[0], coordinates[1], slope)
    return count

def get_next_coordinates(tree_map, row, col, slope):
    new_row = row + slope[0] 
    if (new_row >= len(tree_map)):
        return (len(tree_map),0)

    new_col = 0
    if (col + slope[1] < len(tree_map[new_row])):
        new_col = col + slope[1]
    else:
        new_col = col + slope[1] - len(tree_map[new_row]) 
    return (new_row, new_col)

def is_tree(x):
    return x == '#'

if __name__ == '__main__':
    tree_map = get_tree_map()
    slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]

    total = 1
    for slope in slopes:
        count = count_trees(tree_map, slope)
        total *= count

    print(total)

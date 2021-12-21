def get_input():
    f = open("input.txt")
    raw_lines = [line.strip().split(" -> ") for line in f.readlines()]
    lines = []
    for line in raw_lines:
        coord_1, coord_2 = line
        x1, y1 = coord_1.split(",")
        x2, y2 = coord_2.split(",")
        lines.append([(int(x1), int(y1)), (int(x2), int(y2))])
    f.close()
    return lines


def get_max_x(lines):
    max_x = 0
    for line in lines:
        if line[0][0] > max_x:
            max_x = line[0][0]
        if line[1][0] > max_x:
            max_x = line[1][0]
    return max_x


def get_max_y(lines):
    max_y = 0
    for line in lines:
        if line[0][1] > max_y:
            max_y = line[0][1]
        if line[1][1] > max_y:
            max_y = line[1][1]
    return max_y


def get_base_grid(max_x, max_y):
    return [[0 for _ in range(max_x)] for _ in range(max_y)]


def enumerate_points(line):
    p1, p2 = line
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        if y2 > y1:
            return [(x1, i) for i in range(y1, y2 + 1)]
        else:
            return [(x1, i) for i in range(y2, y1 + 1)]
    elif y1 == y2:
        if x2 > x1:
            return [(i, y1) for i in range(x1, x2 + 1)]
        else:
            return [(i, y1) for i in range(x2, x1 + 1)]
    else:
        num_iter = abs(x2 - x1) + 1
        if x1 > x2 and y1 < y2:
            return [(x1 - i, y1 + i) for i in range(num_iter)]
        elif x1 > x2 and y1 > y2:
            return [(x1 - i, y1 - i) for i in range(num_iter)]
        if x1 < x2 and y1 < y2:
            return [(x1 + i, y1 + i) for i in range(num_iter)]
        elif x1 < x2 and y1 > y2:
            return [(x1 + i, y1 - i) for i in range(num_iter)]
    return []


def mark_grid(grid, line):
    points = enumerate_points(line)
    for point in points:
        x, y = point
        grid[y][x] += 1
    return


def count_intersections(grid):
    count = 0
    for row in grid:
        for item in row:
            if item != "." and item >= 2:
                count += 1
    return count


if __name__ == "__main__":
    lines = get_input()
    max_x = get_max_x(lines)
    max_y = get_max_y(lines)
    grid = get_base_grid(max_x + 1, max_y + 1)

    for line in lines:
        mark_grid(grid, line)

    num_intersections = count_intersections(grid)
    print(num_intersections)

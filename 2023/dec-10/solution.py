# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

import pytest


def get_next_steps_from_pipe(pipe, x, y):
    if pipe == "|":
        return ((x - 1, y), (x + 1, y))
    if pipe == "-":
        return ((x, y - 1), (x, y + 1))
    if pipe == "L":
        return ((x - 1, y), (x, y + 1))
    if pipe == "J":
        return ((x - 1, y), (x, y - 1))
    if pipe == "7":
        return ((x, y - 1), (x + 1, y))
    if pipe == "F":
        return ((x + 1, y), (x, y + 1))
    raise f"Cannot find next steps for {pipe} at {x},{y}"


def get_next_step_from_start(grid, x, y):
    # Check if east is a valid grid pos and has a valid pipe
    # Then south, west, north
    if (y + 1 == len(grid[x]) - 1 and grid[x][y + 1] in ("7", "J")) or (
        y + 1 < len(grid[x]) - 1 and grid[x][y + 1] in ("-", "7", "J")
    ):
        return (x, y + 1)
    if (x + 1 == len(grid) - 1 and grid[x + 1][y] in ("L", "J")) or (
        x + 1 < len(grid) - 1 and grid[x + 1][y] in ("|", "L", "J")
    ):
        return (x + 1, y)
    if (y - 1 == 0 and grid[x][y - 1] in ("L", "F")) or (
        y - 1 > 0 and grid[x][y - 1] in ("-", "L", "F")
    ):
        return (x, y - 1)
    if (x - 1 == 0 and grid[x - 1][y] in ("7", "F")) or (
        x - 1 > 0 and grid[x - 1][y] in ("|", "7", "F")
    ):
        return (x - 1, y)
    raise f"Cannot find next pos for start at ({x},{y})"


if __name__ == "__main__":
    grid = [[c for c in line.strip()] for line in open("input.txt").readlines()]

    start_pos = (0, 0)
    for i, row in enumerate(grid):
        if "S" in row:
            start_pos = (i, row.index("S"))

    num_steps = 0
    prev_x, prev_y = start_pos
    x, y = get_next_step_from_start(grid, prev_x, prev_y)
    while grid[x][y] != "S":
        pos1, pos2 = get_next_steps_from_pipe(grid[x][y], x, y)
        if (prev_x, prev_y) == pos1:
            prev_x, prev_y = x, y
            x, y = pos2
        else:
            prev_x, prev_y = x, y
            x, y = pos1

        num_steps += 1

    # Add the final uncounted step back to S
    print((num_steps + 1) / 2)


@pytest.mark.parametrize(
    "pipe,x,y,expected",
    [
        ("F", 1, 1, ((2, 1), (1, 2))),
        ("L", 3, 1, ((2, 1), (3, 2))),
        ("J", 3, 3, ((2, 3), (3, 2))),
        ("7", 1, 3, ((1, 2), (2, 3))),
        ("|", 2, 1, ((1, 1), (3, 1))),
        ("-", 1, 2, ((1, 1), (1, 3))),
    ],
)
def test_get_next_steps_from_pipe(pipe, x, y, expected):
    assert get_next_steps_from_pipe(pipe, x, y) == expected

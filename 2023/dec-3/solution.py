import pytest

part_numbers = {}  # { [row-col: str]: part number str }
symbols = {}  # { [row-col: str]: bool for isSymbol }
max_row_idx = 0
max_col_idx = 0


def build_dicts():
    for row, line in enumerate(lines):
        line = line.strip()
        col = 0
        while col < len(line):
            if line[col].isdigit():
                part_number = ""
                while col < len(line) and line[col].isdigit():
                    part_number += line[col]
                    symbols[f"{row}-{col}"] = is_symbol(line[col])
                    col += 1
                part_numbers[f"{row}-{col - len(part_number)}"] = part_number
            else:
                symbols[f"{row}-{col}"] = is_symbol(line[col])
                col += 1


def get_indices_to_check(row: int, col: int, length: int, max_row: int, max_col: int):
    indices = []

    # Check all indices above and diagonal to the part number
    if row > 0:
        if col > 0:
            indices.append(f"{row-1}-{col-1}")
        indices.extend([f"{row-1}-{col+idx}" for idx in range(length)])
        if (col + length - 1) < max_col:
            indices.append(f"{row-1}-{col+length}")
    # Check indices next to part number
    if col > 0:
        indices.append(f"{row}-{col-1}")
    if (col + length - 1) < max_col:
        indices.append(f"{row}-{col+length}")
    # Check all indices below and diagonal to the part number
    if row < max_row:
        if col > 0:
            indices.append(f"{row+1}-{col-1}")
        indices.extend([f"{row+1}-{col+idx}" for idx in range(length)])
        if (col + length - 1) < max_col:
            indices.append(f"{row+1}-{col+length}")

    return indices


def is_adjacent_to_symbol(row_col):
    row, col = (int(d) for d in row_col.split("-"))
    return any(
        symbols[idx]
        for idx in get_indices_to_check(
            row, col, len(part_numbers[row_col]), max_row_idx, max_col_idx
        )
    )


def is_symbol(c: str):
    return not c.isalnum() and c != "."


def sum_part_numbers_adjacent_to_symbols():
    return sum(
        [
            int(part_numbers[row_col])
            for row_col in part_numbers.keys()
            if is_adjacent_to_symbol(row_col)
        ]
    )


if __name__ == "__main__":
    lines = open("input.txt").readlines()
    max_row_idx, max_col_idx = len(lines) - 1, len(lines[0].strip()) - 1

    build_dicts()

    # Part 1
    print(sum_part_numbers_adjacent_to_symbols())

    # Part 2


@pytest.mark.parametrize(
    "input,expected",
    [
        ("a", False),
        ("A", False),
        ("6", False),
        (".", False),
        ("$", True),
        ("#", True),
        ("/", True),
        ("=", True),
        ("*", True),
        ("-", True),
        ("&", True),
        ("%", True),
        ("@", True),
        ("+", True),
    ],
)
def test_is_symbol(input, expected):
    assert is_symbol(input) == expected


@pytest.mark.parametrize(
    "row,col,length,max_row,max_col,expected_indices",
    [
        (0, 0, 3, 9, 9, set(["0-3", "1-0", "1-1", "1-2", "1-3"])),
        (
            0,
            5,
            3,
            9,
            9,
            set(["0-4", "0-8", "1-4", "1-5", "1-6", "1-7", "1-8"]),
        ),
        (0, 0, 2, 2, 3, set(["0-2", "1-0", "1-1", "1-2"])),
        (0, 1, 2, 2, 3, set(["0-0", "0-3", "1-0", "1-1", "1-2", "1-3"])),
        (0, 2, 2, 2, 3, set(["0-1", "1-1", "1-2", "1-3"])),
        (1, 0, 2, 2, 3, set(["0-0", "0-1", "0-2", "1-2", "2-0", "2-1", "2-2"])),
        (
            1,
            1,
            2,
            2,
            3,
            set(["0-0", "0-1", "0-2", "0-3", "1-0", "1-3", "2-0", "2-1", "2-2", "2-3"]),
        ),
        (1, 2, 2, 2, 3, set(["0-1", "0-2", "0-3", "1-1", "2-1", "2-2", "2-3"])),
        (2, 0, 2, 2, 3, set(["2-2", "1-0", "1-1", "1-2"])),
        (2, 1, 2, 2, 3, set(["2-0", "2-3", "1-0", "1-1", "1-2", "1-3"])),
        (2, 2, 2, 2, 3, set(["2-1", "1-1", "1-2", "1-3"])),
    ],
)
def test_get_indices_to_check(row, col, length, max_row, max_col, expected_indices):
    assert (
        set(get_indices_to_check(row, col, length, max_row, max_col))
        == expected_indices
    )

def get_input():
    f = open("input.txt")
    nums = f.readline().strip().split(",")
    nums = [int(n) for n in nums]

    boards = []
    line = f.readline()
    line = f.readline().strip()
    while line != "":
        board = []
        while line != "":
            line = line.strip().split(" ")
            board_row = [
                {"value": int(num.strip()), "marked": False}
                for num in line
                if num != ""
            ]
            board.append(board_row)
            line = f.readline().strip()
        boards.append(board)
        line = f.readline().strip()

    f.close()
    return nums, boards


def mark_boards(boards, num):
    for board in boards:
        for row in board:
            for item in row:
                if item.get("value") == num:
                    item["marked"] = True


def check_rows(board):
    for row in board:
        if all([item["marked"] for item in row]):
            return True
    return False


def check_cols(board):
    for i in range(5):
        items = [row[i] for row in board]
        if all([item["marked"] for item in items]):
            return True
    return False


def check_for_winners(boards, record=None):
    winners = []
    for idx, board in enumerate(boards):
        if check_rows(board) or check_cols(board):
            winners.append(board)
            if record:
                record[idx] = True
    return None if len(winners) == 0 else winners[0]


def sum_unmarked_nums(board):
    sum = 0
    for row in board:
        for item in row:
            if not item["marked"]:
                sum += item["value"]
    return sum


if __name__ == "__main__":
    # Part 1
    nums, boards = get_input()

    for num in nums:
        mark_boards(boards, num)
        winning_board = check_for_winners(boards)
        if winning_board:
            sum = sum_unmarked_nums(winning_board)
            print(sum * num)
            break

    # Part 2
    nums, boards = get_input()
    record = [False for _ in boards]
    last_to_win = None
    for num in nums:
        mark_boards(boards, num)
        check_for_winners(boards, record)
        if record.count(False) == 1:
            last_to_win = boards[record.index(False)]
        elif record.count(False) == 0:
            sum = sum_unmarked_nums(last_to_win)
            print(sum * num)
            break

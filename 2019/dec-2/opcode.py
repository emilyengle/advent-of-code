code = []


def add(op1, op2, result_idx):
    result = code[op1] + code[op2]
    code[result_idx] = result


def mult(op1, op2, result_idx):
    result = code[op1] * code[op2]
    code[result_idx] = result


def eval_code(instruction, op1, op2, result_idx):
    if instruction == 1:
        add(op1, op2, result_idx)
    elif instruction == 2:
        mult(op1, op2, result_idx)


def eval_prog():
    for i in range(0, len(code), 4):
        instruction, op1, op2, result_idx = get_instructions(i)
        if instruction == 99:
            return
        eval_code(instruction, op1, op2, result_idx)


def get_code():
    file = open('input.txt', 'r')
    for line in file.readlines():
        global code
        code = line.split(',')
    for i, c in enumerate(code):
        code[i] = int(c)


def get_instructions(idx):
    return int(code[idx]), int(code[idx + 1]), int(code[idx + 2]), int(code[idx + 3])


def main():
    get_code()

    for noun in range(0, 100):
        for verb in range(0, 100):
            get_code()
            code[1] = noun
            code[2] = verb

            eval_prog()
            if code[0] == 19690720:
                print(100 * noun + verb)
                break


main()

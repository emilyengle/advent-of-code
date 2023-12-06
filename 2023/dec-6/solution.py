import math


def quadratic_formula(a, b, c):
    root1 = ((-1 * b) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    root2 = ((-1 * b) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    return root1, root2


if __name__ == "__main__":
    # Part 1
    time, distance = [
        line.strip().split(":")[1].strip() for line in open("input.txt").readlines()
    ]
    times = [int(t.strip()) for t in time.split(" ") if t.strip()]
    distances = [int(d.strip()) for d in distance.split(" ") if d.strip()]

    prod = 1
    for i, time in enumerate(times):
        distance = distances[i]
        ways_to_win = sum(1 for t in range(time + 1) if (t * (time - t)) > distance)
        prod *= ways_to_win

    print(prod)

    # Part 2
    time = 71530
    distance = 940200
    # time = 48989083
    # distance = 390110311121360

    # system of equations !
    # t1 * (t2 - t1) = 940200
    #      - t1^2 + t1t2 - 940200 = 0
    #      - t1^2 + (71530 - t1)t1 - 940200 = 0
    #      - t1^2 + 71530t1 - t1^2 - 940200 = 0
    #      - 2t1^2 + (time)t1 - distance = 0

    # t1 + t2 = 71530
    #     t2 = 71530 - t1

    # discriminant: b^2 - 4ac
    discriminant = (time * time) - (4 * -2 * -1 * distance)
    print(f"Discriminant: {discriminant}")

    # quadratic roots
    roots = quadratic_formula(-2, time, -1 * distance)
    root1 = math.ceil(min(roots))
    root2 = math.floor(max(roots))
    print(f"Roots: {root1, root2}")
    print(f"Total ways to win: {root2 - root1 + 1}")

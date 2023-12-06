import math


def get_discriminant(a, b, c):
    return (b * b) - (4 * a * c)


def get_roots(a, b, c):
    discriminant = get_discriminant(a, b, c)
    root1 = ((-1 * b) + math.sqrt(discriminant)) / (2 * a)
    root2 = ((-1 * b) - math.sqrt(discriminant)) / (2 * a)
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
    # time = 71530
    # distance = 940200
    time = 48989083
    distance = 390110311121360

    # quadratic equation !
    # t1 * (t - t1) = d
    #      -t1^2 + (t)t1 = d
    #      t1^2 - (t)t1 + d = 0

    # discriminant: b^2 - 4ac
    print(f"Discriminant: {get_discriminant(1, time * -1, distance)}")

    # quadratic roots
    roots = get_roots(1, time * -1, distance)
    root1 = math.ceil(min(roots))
    root2 = math.floor(max(roots))
    print(f"Roots: {roots}")
    print(f"Total ways to win: {root2 - root1 + 1}")

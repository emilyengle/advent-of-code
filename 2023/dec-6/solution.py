if __name__ == "__main__":
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

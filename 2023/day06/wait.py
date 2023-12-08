from math import ceil, floor
def run():
    with open("input.txt", "r") as f:
        times = [int("".join(f.readline().split()[1:]))]
        distances = [int("".join(f.readline().split()[1:]))]

    print(times)
    print(distances)

    combos = []

    for time, dist in zip(times, distances):
        # h(time-h) > dist
        # -h**2 + h*time - dist > 0

        # a = -1, b = time, c = -dist
        # b^2 - 4*dist
        det = time*time - 4*dist
        if det < 0:
            combos.append(0)
            continue

        min = ceil(time/2 - det**.5/2)
        max = floor(time/2 + det**.5/2)

        combos.append(max-min+1)

    print(combos)
    prod = 1
    for combo in combos:
        prod *= combo
    print(prod)

  


if __name__ == "__main__":
    run()
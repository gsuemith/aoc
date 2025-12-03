from collections import defaultdict

def run():

    with open("input.txt", "r") as f:
        lines = f.readlines()

    data = []

    for line in lines:
        levels = [int(l) for l in line.strip().split(" ")]
        safe = False
        dampened = False
        positive = levels[1] - levels[0] > 0
        for i in range(len(levels)):
            safe = safe or helper(levels[:i] + levels[i+1:])
            if safe:
                break
        data.append(safe)

    print(sum(data))

def helper(levels):
    if levels[1] - levels[0] == 0:
        return False
    positive = levels[1] - levels[0] > 0
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if 1 <= abs(diff) <= 3 and (positive and diff > 0 or not positive and diff < 0):
            continue
        else:
            return False

    return True

if __name__ == "__main__":
    run()
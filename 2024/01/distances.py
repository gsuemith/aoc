from collections import defaultdict

def run():

    with open("input.txt", "r") as f:
        lines = f.readlines()

    left = []
    b_counts = defaultdict(int)

    for line in lines:
        a, b = line.strip().split("   ")
        b_counts[int(b)] += 1
        left.append(int(a))


    total = 0
    for n in left:
        total += n * b_counts[n]

    print(total)

if __name__ == "__main__":
    run()
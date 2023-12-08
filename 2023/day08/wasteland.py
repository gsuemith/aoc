def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    dirs = lines[0].strip()

    graph = {}

    for line in lines[2:]:
        mapping = [x.strip() for x in line.split("=")]
        graph[mapping[0]] = {"L":mapping[1][1:4],"R":mapping[1][6:9]}

    node = 'AAA'
    step = 0

    while node != 'ZZZ':
        dir = dirs[step % len(dirs)]
        step += 1
        node = graph[node][dir]

    print(step)

if __name__ == "__main__":
    run()
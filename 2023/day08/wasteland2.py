def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    dirs = lines[0].strip()

    graph = {}

    for line in lines[2:]:
        mapping = [x.strip() for x in line.split("=")]
        graph[mapping[0]] = {"L":mapping[1][1:4],"R":mapping[1][6:9]}

    nodes = [key for key in graph.keys() if key[-1] == 'A']
    len_nodes = len(nodes)
    print(nodes)
    step = 0

    while sum(x[-1] == 'Z' for x in nodes) != len_nodes:
        dir = dirs[step % len(dirs)]
        step += 1
        for i in range(len(nodes)):
            nodes[i] = graph[nodes[i]][dir]
        print(nodes)

    print(step)

if __name__ == "__main__":
    run()
from math import lcm

def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    dirs = lines[0].strip()

    graph = {}

    for line in lines[2:]:
        mapping = [x.strip() for x in line.split("=")]
        graph[mapping[0]] = {"L":mapping[1][1:4],"R":mapping[1][6:9]}

    nodes = [key for key in graph.keys() if key[-1] == 'A']
    cycle_tracker = [[set(), 0] for _ in nodes]
    len_nodes = len(nodes)
    print(nodes)
    step = 0
    cycles = []

    for i in range(len(nodes)):
        step = 0

        node = nodes[i]

        while True:
            dir = dirs[step % len(dirs)]
            node = graph[node][dir]

            if node[-1] == 'Z':
                node_z = (node, step%len(dirs))
                if node_z in cycle_tracker[i][0]:
                    break
                cycle_tracker[i][0].add((node, step%len(dirs)))
                cycle_tracker[i][1] = step

            step += 1

        cycle_tracker[i].append((cycle_tracker[i][1] + 1) // len(dirs))
        cycles.append(cycle_tracker[i])
            
    print(len(dirs))
    print(cycles)
    periods = [x[-1]*len(dirs) for x in cycles]
   
    print(lcm(*periods))

if __name__ == "__main__":
    run()
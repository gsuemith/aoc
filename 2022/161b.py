from copy import deepcopy

def run():
    with open("16.txt", "r") as f:
        lines = f.readlines()

    graph = {}

    for line in lines:
        items = line.split()
        graph[items[1]] = {
            "rate": int(items[4][5:-1]),
            "neighbors": [valve[:2] for valve in items[9:]]
        }
    good_valves = {key for key,value in graph.items() if value["rate"]}
    dist_mat = {valve: {next_valve: 0 for next_valve in good_valves} for valve in good_valves}
    for a, valves in dist_mat.items():
        for b, dist in valves.items():
            if b == a or dist:
                continue
            dist_mat[b][a] = valves[b] = distance(a,b, graph)
    

    start = 'AA'
    start_dists = {valve: distance(start, valve, graph) for valve in good_valves}

    rate = 0
    released = 0
    minutes = 30
    valve_on = {valve:False for valve in good_valves}
    valve_on[start] = False

    print(traverse(start, start_dists, dist_mat, graph, rate, released, minutes, valve_on))

def distance(a, b, graph):
    visited = {key: False for key in graph.keys()}
    queue = [(a,0)]

    while len(queue) > 0:
        current, dist = queue.pop(0)
        if current == b:
            return dist
        if visited[current]:
            continue
        visited[current] = True
        for n in graph[current]["neighbors"]:
            queue.append((n,dist+1))
        

def traverse(current, distances, dist_mat, graph: dict, rate, released, minutes, valve_on: dict):
    if minutes == 0 or all(valve_on.values()):
        return released + rate*minutes
    
    valve_on[current] = True
    rate += graph[current]["rate"]

    options = []
    for valve, dist in distances.items():
        if dist + 1 > minutes - 1 or valve == current or valve_on[valve]:
            continue
        options.append(traverse(valve, dist_mat[valve], dist_mat, graph, rate, released+(dist+1)*rate, minutes-dist-1, {**valve_on}))

    return max(options) if options else released + rate*minutes


if __name__ == "__main__":
    run()
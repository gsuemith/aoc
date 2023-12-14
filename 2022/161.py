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

    current = 'AA'
    rate = 0
    released = 0
    minutes = 30
    valve_on = {key:False for key in graph.keys()}
    visited = {key:False for key in graph.keys()}

    print(traverse(current, graph, rate, released, minutes, valve_on, visited))

def traverse(current, graph: dict, rate, released, minutes, valve_on, visited):
    if minutes == 0:
        print()
        return (released, rate, current)
    
    
    

    if graph[current]["rate"] and not valve_on[current]:
        released += rate
        minutes -= 1
        if minutes == 0:
            return (released, rate, current)
        rate += graph[current]["rate"]
        valve_on[current] = True
        visited = {key:False for key in graph.keys()}
    
    released += rate
    visited[current] = True

    options = []
    for n in graph[current]["neighbors"]:
        if visited[n]:
            continue
        options.append(traverse(n, graph, rate, released, minutes-1, {**valve_on}, {**visited}))

    if len(options) == 0:
        visited = {key:False for key in graph.keys()}
        visited[current] = True
        for n in graph[current]["neighbors"]:
            if visited[n]:
                continue
            options.append(traverse(n, graph, rate, released, minutes-1, {**valve_on}, {**visited}))

    print(options)
    return max(options)



if __name__ == "__main__":
    run()
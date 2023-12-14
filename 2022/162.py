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
    good_valves = {key:0 for key,value in graph.items() if value["rate"]}
    dist_mat = {valve: {next_valve: 0 for next_valve in good_valves.keys()} for valve in good_valves}
    for a, valves in dist_mat.items():
        for b, dist in valves.items():
            if b == a or dist:
                continue
            dist_mat[b][a] = valves[b] = distance(a,b, graph)
    


    start_dists = {valve: distance('AA', valve, graph) for valve in good_valves}
    valve_list = list(good_valves.keys())
    starts = []
    for i, valve_1 in enumerate(valve_list):
        for valve_2 in valve_list[i+1:]:
            starts.append([
                (valve_1, start_dists[valve_1]),
                (valve_2, start_dists[valve_2]),
                {**good_valves}
            ])


    rate = 0
    released = 0
    minutes = 26
    # valve_on = {valve:False for valve in good_valves}
    # valve_on[start] = False

    # print(traverse(start, start_dists, dist_mat, graph, rate, released, minutes, valve_on))
    

    options = []
    print(len(starts))
    for start in starts:
        print(start)
        options.append(traverse(start, dist_mat, graph))

    print(options)
    print(max(options))
    
def traverse(next_nodes, dist_mat, graph, minutes=26):
    valve_1, valve_2, valve_states = next_nodes
    
    if valve_1[1] == valve_2[1]:
        options = []
        for next_valve, rate in valve_states.items():
            if rate:
                continue
            on_time = minutes - valve_1[1] - 1
            dist_1, dist_2 = dist_mat[valve_1[0]][next_valve], dist_mat[valve_2[0]][next_valve]
            if dist_1 <= dist_2:
                eta = valve_1[1] + 1 + dist_1
                valve_states_copy = {**valve_states}
                valve_states_copy[valve_1[0]] = on_time
                options.append(traverse(
                    [(next_valve, eta), valve_2, valve_states_copy],
                    dist_mat, graph
                ))
            else:
                eta = valve_2[1] + 1 + dist_2
                valve_states_copy = {**valve_states}
                valve_states_copy[valve_1[0]] = on_time
                options.append(traverse(
                    [(next_valve, eta), valve_2, valve_states_copy],
                    dist_mat, graph
                ))
        return max(options)



    current_idx, later_idx = (0, 1) if valve_1[1] < valve_2[1] else (1, 0) 
    current, later = next_nodes[current_idx], next_nodes[later_idx]

    

    curr_valve, travel_time = current
    
    if travel_time >= minutes or all(valve_states.values()):
        released = 0
        for valve, time in valve_states.items():
            released += time * graph[valve]["rate"]

        # print(*list(f"{val:2} {graph[valve]['rate']:2}, " for valve, val in valve_states.items()))
        return released

    valve_states[curr_valve] = minutes - travel_time - 1

    options = []
    remaining_valves = [valve for valve, rate in valve_states.items() if rate == 0]
    for next_valve in remaining_valves:
        eta = travel_time + 1 + dist_mat[curr_valve][next_valve]
        options.append(traverse(
            [(next_valve, eta), later, {**valve_states}],
            dist_mat, graph
        ))

    if options:
        return(max(options))
    
    valve_states[later[0]] = minutes - later[1] - 1
    released = 0
    for valve, time in valve_states.items():
        released += time * graph[valve]["rate"]

    return released



    

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
        

# def traverse(current, distances, dist_mat, graph: dict, rate, released, minutes, valve_on: dict):
#     if minutes == 0 or all(valve_on.values()):
#         return released + rate*minutes
    
#     valve_on[current] = True
#     rate += graph[current]["rate"]

#     options = []
#     for valve, dist in distances.items():
#         if dist + 1 > minutes - 1 or valve == current or valve_on[valve]:
#             continue
#         options.append(traverse(valve, dist_mat[valve], dist_mat, graph, rate, released+(dist+1)*rate, minutes-dist-1, {**valve_on}))

#     return max(options) if options else released + rate*minutes


if __name__ == "__main__":
    run()
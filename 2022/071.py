def run():
    with open("07.txt", "r") as f:
        lines = f.readlines()

    root = {"size": 0}
    node = root

    for line in lines:
        commands = line.split()

        if commands[0] == "$":
            if commands[1] == "cd":
                node = root if commands[2] == "/" else node[commands[2]]
        elif commands[0] == "dir":
            node[commands[1]] = {"size": 0, "..": node}
        else:
            node["size"] += int(commands[0])

    candidates = []
    update_size(root, candidates)
    print(root["size"])
    space_needed = 30000000 - (70000000 - root["size"])
    print(space_needed)

    print(find_dir_to_delete(root, space_needed))
    

def find_dir_to_delete(node, space_needed):
    best_size = node["size"]

    for name, dir in node.items():
        if name in {"size", ".."}:
            continue
        if dir["size"] >= space_needed:
            best_size = min(best_size, find_dir_to_delete(dir, space_needed))

    return best_size


def update_size(node, candidates):
    for name, dir in node.items():
        if name in {"size", ".."}:
            continue
        node["size"] += update_size(dir, candidates)
    
    if node["size"] <= 100000:
        candidates.append(node["size"])
    return node["size"]



   

if __name__ == "__main__":
    run()
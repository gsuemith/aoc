def run():
    with open("09.txt", "r") as f:
        lines = f.readlines()

    moves = [[int(x) if x.isdigit() else x  for x in line.split()] for line in lines]

    directions = {"R": (0, 1), "L": (0, -1), "U": (1, 1), "D": (1, -1)}
    
    head = [0,0]
    tail = [0,0]

    visited = {tuple(tail)}

    for dir, steps in moves:
        coordinate, increment = directions[dir]
        for _ in range(steps):
            head[coordinate] += increment
            if abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2:
                tail = head.copy()
                tail[coordinate] -= increment
                visited.add(tuple(tail))

    print(len(visited))









if __name__ == "__main__":
    run()
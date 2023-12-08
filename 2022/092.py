def run():
    with open("09.txt", "r") as f:
        lines = f.readlines()

    moves = [[int(x) if x.isdigit() else x  for x in line.split()] for line in lines]

    directions = {"R": (0, 1), "L": (0, -1), "U": (1, 1), "D": (1, -1)}
    
    rope = [[0,0] for _ in range(10)]
    path = []

    visited = {tuple(rope[-1])}
    a = True
    for dir, steps in moves:
        coordinate, increment = directions[dir]
        for _ in range(steps):
            rope[0][coordinate] += increment

            for i in range(1, len(rope)):
                delta_x, delta_y = rope[i-1][0] - rope[i][0], rope[i-1][1] - rope[i][1]
                if abs(delta_x) == 2 or abs(delta_y) == 2:
                    axis = 0 if abs(delta_x) == 2 else 1
                    delta = delta_x//abs(delta_x) if axis == 0 else delta_y//abs(delta_y)
                    rope[i] = rope[i-1].copy()
                    rope[i][axis] -= delta
                    if i == 9:
                        path.append([tuple(rope[i-1]),tuple(rope[i])])

            visited.add(tuple(rope[-1]))

        
        
    print(path)
             
    print(len(visited))










if __name__ == "__main__":
    run()
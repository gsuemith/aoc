reflections = {
    "\\": [[0,1],[1,0]], "/": [[0,-1],[-1,0]]
}
splitters = {
    "|": {(0,1): [[1,0],[-1,0]], (0,-1): [[1,0],[-1,0]]},
    "-": {(1,0): [[0,1],[0,-1]], (-1,0): [[0,1],[0,-1]]},
}

def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [line.strip() for line in lines]
    # for line in grid:
    #     for char in line:
    #         if char == "\\":
    #             print(char)
    r, c = len(grid), len(grid[0])

    starts = []
    for i in range(r):
        starts.extend([[[i,0],[0,1]],[[i,c-1],[0,-1]]])
    for j in range(c):
        starts.extend([[[0,j],[1,0]],[[r-1,j],[-1,0]]])

    most = 0
    for start in starts:
        stack = [start]
        energized = [[False]*c for _ in range(r)]

        while len(stack) > 0:
            pos, dir = stack.pop()
            i, j = pos
            if not (0 <= i < r and 0 <= j < c):
                continue
            if energized[i][j] == dir:
                continue

            char = grid[i][j]
            energized[i][j] = dir

            if char in reflections:
                new_dir = reflect(reflections[char], dir)
                stack.append([add(pos, new_dir), new_dir])
            elif char in splitters and tuple(dir) in splitters[char]:
                stack.extend([add(pos, new_dir), new_dir] for new_dir in splitters[char][tuple(dir)])
            else:
                stack.append([add(pos, dir), dir])

        energy = sum(sum(x is not False for x in row) for row in energized)
        most = max(most, energy)
        print(most, energy, start)

def reflect(mat, dir):
    new_dir = []
    i, j = dir
    for di, dj in mat:
        new_dir.append(i*di + j*dj)

    return new_dir


def add(pos, dir):
    i, j = pos
    di, dj = dir
    return [i+di, j+dj]

    


if __name__ == "__main__":
    run()
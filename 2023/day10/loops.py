from sys import setrecursionlimit

junctions = {
    '|':{(-1,0):(1,0), (1,0):(-1,0)},
    '-':{(0,-1):(0,1), (0,1):(0,-1)},
    'L':{(-1,0):(0,1), (0,1):(-1,0)},
    'J':{(-1,0):(0,-1), (0,-1):(-1,0)},
    '7':{(1,0):(0,-1), (0,-1):(1,0)},
    'F':{(1,0):(0,1), (0,1):(1,0)},
    '.':set(),
    'S':set(),
}

def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [line.strip() for line in lines]
    r, c = len(grid), len(grid[0])
    start = next((i,j) for i in range(r) for j in range(c) if grid[i][j] == 'S')
    setrecursionlimit(r*c)
    
    length = 0
    way1, way2 = (94, 74), (95, 75) #available_next(start, r, c, grid)
    positions = [(start, way1), (start, way2)]
    loop = {start, way1, way2}

    while positions[0][1] != positions[1][1]:
        length += 1
        for i in range(2):
            pos1, pos2 = positions[i]
            positions[i] = (pos2, next_pos(pos1, pos2, grid))
            loop.add(positions[i][1])


    positions = (start, way1)
    left_points = set()
    right_points = set()
    while positions[1] != start:
        pos1, pos2 = positions
        dir = direction(pos1, pos2)
        left1, right1 = left_right(pos1, dir)
        left2, right2 = left_right(pos2, dir)
        left = [left1, left2]
        right = [right1, right2]
        for pos in left:
            if pos not in loop and pos not in left_points:
                dfs(pos, r, c, loop, left_points)
        for pos in right:
            if pos not in loop and pos not in right_points:
                dfs(pos, r, c, loop, right_points)

        positions = [pos2, next_pos(pos1, pos2, grid)]
        

    loop_grid = []
    for i in range(r):
        line = ""
        for j in range(c):
            if (i,j) in loop:
                line += grid[i][j]
            elif (i,j) in left_points:
                line += 'O'
            elif(i,j) in right_points:
                line += "X"
            else:
                line += "."
        loop_grid.append(line)
        print(line)

    print(len(right_points))


def dfs(pos: tuple[int], r, c, loop: set, points: set):
    if pos in loop or pos in points:
        return
    points.add(pos)

    i, j = pos
    neighbors = []
    if i - 1 >= 0:
        neighbors.append((i-1,j))
    if i + 1 < r :
        neighbors.append((i+1,j))
    if j - 1 >= 0:
        neighbors.append((i,j-1))
    if j + 1 < c :
        neighbors.append((i,j+1))

    for n in neighbors:
        dfs(n, r, c, loop, points)


def left_right(pos, dir):
    i,j = pos
    if dir[0]:
        if dir[0] == -1:
            return (i,j-1), (i,j+1)
        return (i,j+1), (i,j-1)
    if dir[1] == 1:
        return (i-1,j), (i+1,j)
    return (i+1,j), (i-1,j)



def direction(pos1, pos2):
    i1, j1 = pos1
    i2, j2 = pos2
    return (i2-i1, j2-j1)


def next_pos(last, current, grid):
    ic, jc = current
    delta_in = (last[0]-ic, last[1] - jc)
    i_out, j_out = junctions[grid[ic][jc]][delta_in]

    return (ic + i_out, jc + j_out)
    


if __name__ == "__main__":
    run()
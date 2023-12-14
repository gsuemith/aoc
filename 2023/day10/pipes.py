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
    
    length = 0
    way1, way2 = (94, 74), (95, 75) #available_next(start, r, c, grid)
    positions = [(start, way1), (start, way2)]

    while positions[0][1] != positions[1][1]:
        length += 1
        for i in range(2):
            pos1, pos2 = positions[i]
            positions[i] = (pos2, next_pos(pos1, pos2, grid))

    print(positions, length+1)

def next_pos(last, current, grid):
    ic, jc = current
    delta_in = (last[0]-ic, last[1] - jc)
    i_out, j_out = junctions[grid[ic][jc]][delta_in]

    return (ic + i_out, jc + j_out)
    
# def available_next(pos, r, c, grid):
#     i, j = pos
    
#     connections = []
#     if i-1 >= 0 and connected(pos, (i-1, j), grid):
#         connections.append((i-1, j))
#     if i+1 < r and connected(pos, (i+1,j), grid):
#         connections.append((i+1,j))
#     if j-1 >= 0 and connected(pos, (i, j-1), grid):
#         connections.append((i, j-1))
#     if j+1 < c and connected(pos, (i,j+1), grid):
#         connections.append((i,j+1))

#     return connections[0], connections[1]

# def connected(pos1, pos2, grid):
#     i1,j1 = pos1
#     i2,j2 = pos2
#     delta = (pos2[0] - pos1[0], pos2[1] - pos2[1])

#     return delta in junctions[grid[i2][j2]]


if __name__ == "__main__":
    run()
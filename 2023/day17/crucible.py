from .heap import MinHeap

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [[int(x) for x in line.strip()] for line in lines]
    r, c = len(grid), len(grid[0])
    max_heat = sum(sum(row) for row in grid)

    nodes = [[{
        (0,1): [
            [[(1,0),0],[(-1,0),0],[(0,1),1]],
            [[(1,0),0],[(-1,0),0],[(0,1),2]],
            [[(1,0),0],[(-1,0),0]]
        ],
        (1,0): [
            [[(0,-1),0],[(0,1),0],[(1,0),1]],
            [[(0,-1),0],[(0,1),0],[(1,0),2]],
            [[(0,-1),0],[(0,1),0]]
        ],
        (0,-1): [
            [[(1,0),0],[(-1,0),0],[(0,-1),1]],
            [[(1,0),0],[(-1,0),0],[(0,-1),2]],
            [[(1,0),0],[(-1,0),0]]
        ],
        (-1,0): [
            [[(0,-1),0],[(0,1),0],[(-1,0),1]],
            [[(0,-1),0],[(0,1),0],[(-1,0),2]],
            [[(0,-1),0],[(0,1),0]]
        ],
    } for _ in range(c)] for _ in range(r)]

    heap = MinHeap(nodes, max_heat)

    
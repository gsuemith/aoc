def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [line.strip() for line in lines]
    r, c  = len(grid), len(grid[0])
    
    grid = rotate_ccw(grid)
    history = {}

    for round in range(10**3): #
        for _ in range(4):
            grid = tilt_rotate(grid)
        tuple_grid = tuple(grid)
        if tuple_grid not in history:
            history[tuple_grid] = []
        history[tuple_grid].append(round)
        if round % 102 == 159 % 102:
            print("\n\n")
            for line in grid:
                print(line)
        if round == 159 + 102*2:
            break
    
    print("\n\n")
    for line in grid:
        print(line)

    total = 0
    for line in grid:
        total += sum(100-i for i, char in enumerate(line) if char == "O")

    print(total)

def rotate_ccw(grid):
    rot_grid = []
    for j in range(99, -1, -1):
        rot_grid.append("".join(grid[i][j] for i in range(100)))

    return rot_grid

def tilt_rotate(grid):
    new_grid = []
    for line in grid:
        new_line = []
        start = 0
        count_rock = 0
        count_dot = 0
        for j in range(100):
            if line[j] == "#":
                new_line.append("O"*count_rock)
                new_line.append("."*count_dot)
                new_line.append("#")
                start = j+1
                count_rock, count_dot = 0,0
            elif line[j] == "O":
                count_rock += 1
            else:
                count_dot += 1

        new_line.append("O"*count_rock)
        new_line.append("."*count_dot)
        new_line = "".join(new_line)
        if len(new_line) != 100:
            print(len(new_line))
            break
        new_grid.append(new_line)

    rot_grid = []
    for j in range(100):
        rot_grid.append("".join(new_grid[i][j] for i in range(99,-1,-1)))
        
    return rot_grid

    

if __name__ == "__main__":
    run()
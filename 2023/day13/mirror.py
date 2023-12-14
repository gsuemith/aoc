def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grids = []
    grid = []
    for line in lines:
        if line == "\n":
            grids.append(grid)
            grid = []
            continue
        grid.append(line.strip())
    grids.append(grid)

    reflections = []
    for grid in grids[:]:
        r, c = len(grid), len(grid[0])
        reflection = None
        for j in range(1,c):
            size = min(c-j, j)
            start = j-size-1
            end = j+size
            if grid[0][j:end] == grid[0][j-1:None if start < 0 else start:-1]:
                if all(line[j:end] == line[j-1:None if start < 0 else start:-1] for line in grid):
                    reflection = j
                    break

        # print(reflection)
        if not reflection:
            for i in range(1,r):
                size = min(r-i, i)
                start = i-size-1
                end = i+size
                if "".join(grid[y][0] for y in range(i,end)) == "".join(grid[y][0] for y in range(i-1,start,-1)):
                    print("".join(grid[y][0] for y in range(i,end)), "".join(grid[y][0] for y in range(i-1,start,-1)))
                    if all("".join(grid[y][j] for y in range(i,end)) == "".join(grid[y][j] for y in range(i-1,start,-1)) for j in range(c)):
                        reflection = i*100
                        break
        reflections.append(reflection)

    
    print(reflections)
    print(sum(reflections))

        



if __name__ == "__main__":
    run()
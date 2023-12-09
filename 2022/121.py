def run():
    with open("12.txt", "r") as f:
        lines = f.readlines()

    ends = {"S": 'a', "E": 'z'}
    heights = {char: height for height, char in enumerate("abcdefghijklmnopqrstuvwxyz")}

    assert len(heights) == 26

    grid = [list(line.strip()) for line in lines]
    r, c = len(grid), len(grid[0])

    for i in range(r):
        for j in range(c):
            if grid[i][j] in ends:
                char = ends[grid[i][j]]
                ends[grid[i][j]] = (i,j)
                grid[i][j] = char
            grid[i][j] = heights[grid[i][j]]

    print(ends.values())
    start = ends['S']
    end = ends['E']

    queue = [(*start,0,[[False]*c for _ in range(r)])]
    steps = 0

    while len(queue) > 0:
        i, j, step, visited = queue.pop(0)

        if visited[i][j]:
            continue
        visited[i][j] = True

        if (i,j) == end:
            steps = step
            break

        queue.extend(next_steps(i,j,step+1,r,c,visited,grid))

    print(steps)

def next_steps(i,j,step,r,c,visited,grid):
    available = []

    if i-1 >= 0 and not visited[i-1][j] and grid[i][j] + 1 >= grid[i-1][j]:
        available.append((i-1,j, step, visited))
    if i+1 < r and not visited[i+1][j] and grid[i][j] + 1 >= grid[i+1][j]:
        available.append((i+1,j, step, visited))
    if j-1 >= 0 and not visited[i][j-1] and grid[i][j] + 1 >= grid[i][j-1]:
        available.append((i,j-1, step, visited))
    if j+1 < c and not visited[i][j+1] and grid[i][j] + 1 >= grid[i][j+1]:
        available.append((i,j+1, step, visited))

    return available








if __name__ == "__main__":
    run()
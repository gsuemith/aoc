from collections import defaultdict

def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [line.strip() for line in lines]
    m, n = len(grid), len(grid[0])
    visited = [[-1] * n for _ in range(m)]

    start = None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "^":
                start = (i, j)
                break
        if start:
            break

    x, y = start
    directions = [-1, 0, 1, 0, -1]
    dir = 0
    total = 0
    while 0 <= x < m and 0 <= y < n:
        if visited[x][y] == -1:
            dx, dy = directions[dir:dir+2]
            if not (0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] == "#"):
                a, b = x, y
                right_dir = (dir + 1) % 4
                rx, ry = directions[right_dir: right_dir + 2]
                while 0 <= a < m and 0 <= b < n and grid[a][b] != "#" and visited[a][b] != right_dir:
                    a, b = a+rx, b+ry
                if 0 <= a < m and 0 <= b < n and grid[a][b] != "#" and visited[a][b] == right_dir:
                    total += 1
                    print(x,y, directions[right_dir:right_dir+2], "*")
            visited[x][y] = dir
        else:
            if (dir + 1) % 4 == visited[x][y]:
                total += 1
                r = visited[x][y]
                print(x,y, directions[r:r+2])

        dx, dy = directions[dir:dir+2]
        if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] == "#":
            dir = (dir + 1) % 4
            dx, dy = directions[dir:dir+2]


        x += dx
        y += dy

    print(total)






if __name__ == "__main__":
    run()
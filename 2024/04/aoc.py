import re

def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [line.strip() for line in lines]

    s = Search(grid)
    s.count_xmas()

    print(s.count)

class Search:
    def __init__(self, grid):
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

    def count_xmas(self):
        m, n = self.m, self.n
        count = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if self.grid[i][j] == "A":
                    for di, dj in self.directions():
                        if self.xmas(i, j, di, dj):
                            count += 1

        self.count = count
        return count

    def xmas(self, i, j, dx, dy):
        ans = True
        if dy == 0:
            ans = ans and self.grid[i+dx][j+1] == self.grid[i+dx][j-1] == "M"
            ans = ans and self.grid[i-dx][j+1] == self.grid[i-dx][j-1] == "S"
        else:
            ans = ans and self.grid[i+1][j+dy] == self.grid[i-1][j+dy] == "M"
            ans = ans and self.grid[i+1][j-dy] == self.grid[i-1][j-dy] == "S"

        return ans

    def directions(self):
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            yield di, dj

if __name__ == "__main__":
    run()
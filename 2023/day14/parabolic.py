def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [line.strip() for line in lines]
    r, c  = len(grid), len(grid[0])
    tilted = [[[r,0]] for _ in range(c)]

    for j in range(c):
        for i in range(r):
            if grid[i][j] == "#":
                tilted[j].append([r-i-1,0])
                continue
            if grid[i][j] == "O":
                tilted[j][-1][1] += 1

    print(sum(sum(weight(stones[0], stones[1]) for stones in column) for column in tilted))
    # for column in tilted:
    #     print(column)
    #     for s in column:
    #         print(weight(s[0], s[1]))

def weight(row, stones):
    return sum(n for n in range(row, row-stones, -1))

if __name__ == "__main__":
    run()
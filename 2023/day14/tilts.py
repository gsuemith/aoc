def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    grid = [line.strip() for line in lines]
    r, c  = len(grid), len(grid[0])
    n_tilt = [set() for _ in range(c)]

    for j in range(c):
        start = r
        count = 0
        for i in range(r):
            if grid[i][j] == "#":
                n_tilt[j].update(range(start, start-count, -1))
                start = r-i-1
                count = 0
                continue
            if grid[i][j] == "O":
                count += 1
        n_tilt[j].update(range(start, start-count, -1))

    w_tilt = [set() for _ in range(r)]
    for i in range(r,0,-1):
        start = 0
        for j in range(c):
            if grid[r-i][j] == "#":
                count = sum(i in n_tilt[x] for x in range(start, j))
                w_tilt[r-i].update(range(start,start+count))
                start = j+1

    s_tilt = [set() for _ in range(c)]
    for j in range(c):
        start = 1
        for i in range(1,r+1):
            if grid[r-i][j] == "#":
                count = sum(j in w_tilt[r-x] for x in range(start, i))
                s_tilt[j].update(range(start, start+count))
                start = i+1

    e_tilt = [set() for _ in range(r)]
    for i in range(r,0,-1):
        start = c - 1
        for j in range(c-1,-1,-1):
            if grid[r-i][j] == "#":
                count = sum(i in s_tilt[x] for x in range(start,j,-1))
                e_tilt[r-i].update(range(start,start-count-1,-1))
                start = j-1

    tilts = {}
    for round in range(1, 1000000000):

        n_tilt = [set() for _ in range(c)]
        for j in range(c):
            start = r
            for i in range(r,0,-1):
                if grid[r-i][j] == "#":
                    count = sum(j in e_tilt[r-x] for x in range(start, r-i, -1))
                    n_tilt[j].update(range(start,start-count-1,-1))
                    start = i-1

        w_tilt = [set() for _ in range(r)]
        for i in range(r,0,-1):
            start = 0
            for j in range(c):
                if grid[r-i][j] == "#":
                    count = sum(i in n_tilt[x] for x in range(start, j))
                    w_tilt[r-i].update(range(start,start+count))
                    start = j+1

        s_tilt = [set() for _ in range(c)]
        for j in range(c):
            start = 1
            for i in range(1,r+1):
                if grid[r-i][j] == "#":
                    count = sum(j in w_tilt[r-x] for x in range(start, i))
                    s_tilt[j].update(range(start, start+count))
                    start = i+1

        e_tilt = [set() for _ in range(r)]
        for i in range(r,0,-1):
            start = c - 1
            for j in range(c-1,-1,-1):
                if grid[r-i][j] == "#":
                    count = sum(i in s_tilt[x] for x in range(start,j,-1))
                    e_tilt[r-i].update(range(start,start-count-1,-1))
                    start = j-1

        tup = tuplify(e_tilt)
        # print(tup)
        # if tup in tilts:
        #     print(tilts[tup], round)
        tilts[tuplify(e_tilt)] = round
        print(round, len(tilts), sum(sum(stacks) for stacks in e_tilt))

            

    print(sum(sum(stacks) for stacks in e_tilt))


def tuplify(tilt):
    tuples = []
    for s in tilt:
        s = list(s)
        s.sort()
        tuples.append(tuple(s))

    return tuple(tuples)


def weight(row, stones):
    return sum(n for n in range(row, row-stones, -1))

if __name__ == "__main__":
    run()
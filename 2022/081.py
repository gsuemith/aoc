
def run():
    with open("08.txt", "r") as f:
        lines = f.readlines()

    forest = [[int(n) for n in line.strip()] for line in lines]
    r = len(forest)
    c = len(forest[0])

    visibility = [[False for _ in range(c)] for _ in range(r)]
    

    for j in range(1,c-1):
        tallest = -1
        for i in range(r):
            height = forest[i][j]
            if height > tallest:
                visibility[i][j] = True
                tallest = height
            if tallest == 9:
                break
            
        
        tallest_from_top, tallest = tallest, -1
        for i in range(r-1, -1, -1):
            height = forest[i][j]
            if height > tallest:
                visibility[i][j] = True
                tallest = height
            if tallest == tallest_from_top:
                break

    for i in range(1,r-1):
        tallest = -1
        for j in range(c):
            height = forest[i][j]
            if height > tallest:
                visibility[i][j] = True
                tallest = height
            if tallest == 9:
                break

        tallest_from_top, tallest = tallest, -1
        for j in range(c-1, -1, -1):
            height = forest[i][j]
            if height > tallest:
                visibility[i][j] = True
                tallest = height
            if tallest == tallest_from_top:
                break
    
    for row in visibility:
        print("".join(["1" if x else "0" for x in row]))

    print(4 + sum([sum(row) for row in visibility]))




if __name__ == "__main__":
    run()
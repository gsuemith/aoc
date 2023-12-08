
def run():
    with open("08.txt", "r") as f:
        lines = f.readlines()

    forest = [[int(n) for n in line.strip()] for line in lines]
    r = len(forest)
    c = len(forest[0])

    # scores = [[0 for _ in range(c)] for _ in range(r)]
    highest = 0
    

    for i in range(1,r-1):
        for j in range(1,c-1):
            height = forest[i][j]

            up, k = 0, i - 1
            while k >= 0 and forest[k][j] < height:
                up += 1
                k -= 1
            if k != -1:
                up += 1

            down, k = 0, i + 1
            while k < r and forest[k][j] < height:
                down += 1
                k += 1
            if k != r:
                down += 1

            left, k = 0, j - 1
            while k >= 0 and forest[i][k] < height:
                left += 1
                k -= 1
            if k != -1:
                left += 1

            right, k = 0, j + 1
            while k < c and forest[i][k] < height:
                right += 1
                k += 1
            if k != c:
                right += 1

            highest = max(highest, up*down*right*left)

    print(highest)

            




if __name__ == "__main__":
    run()
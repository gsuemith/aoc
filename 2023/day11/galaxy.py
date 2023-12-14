def sign(n):
    return -1 if n < 0 else 1 if n > 0 else 0

def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    image = [line.strip() for line in lines]

    r, c = len(image), len(image[0])
    galaxies = []
    for i in range(r):
        for j in range(c):
            if image[i][j] == "#":
                galaxies.append((i,j))

    empty_row = [all(char == "." for char in row) for row in image]
    empty_col = [all(image[i][j] == "." for i in range(r)) for j in range(c)]

    distances = {g: {og: 0 for og  in galaxies} for g in galaxies}

    total = 0
    for idx, g in enumerate(galaxies):
        for og in galaxies[idx+1:]:
            dist = find_dist(g, og, empty_row, empty_col)
            distances[g][og] = distances[og][g] = dist
            total += dist

    # smallest = [min(val for val in value.values() if val > 0) for key, value in distances.items()]
    print(total)

def find_dist(g1, g2, empty_row, empty_col):
    i1, j1 = g1
    i2, j2 = g2
    row_dist, col_dist = abs(i1-i2), abs(j1-j2)
    if sign(i2-i1):
        row_dist += sum(empty_row[i1:i2:sign(i2-i1)])*999999
    if sign(j2-j1):
        col_dist += sum(empty_col[j1:j2:sign(j2-j1)])*999999

    return row_dist + col_dist

    

if __name__ == "__main__":
    run()
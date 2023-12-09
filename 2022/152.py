def run():
    with open("15.txt", "r") as f:
        lines = f.readlines()
    
    connections = []

    for line in lines:
        data = line.split()
        sx, sy, bx, by = data[2][2:-1], data[3][2:-1], data[-2][2:-1], data[-1][2:]
        connections.append([int(c) for c in [sx,sy,bx,by]])

    # x_coords = [x for c in connections for idx, x in enumerate(c) if idx in {0,2}]
    distances = []
    y = 2000000
    covered = set()
    B_in_row = set()
    for sx, sy, bx, by in connections:
        distances.append([(sx, sy), (bx, by), abs(bx-sx) + abs(by-sy)])

    for S, B, MD in distances:
        if B[1] == y:
            B_in_row.add(B)

        if abs(y - S[1]) > MD:
            continue

        for dx in range(1 + MD - abs(y - S[1])):
            covered.add((S[0] + dx,y))
            covered.add((S[0] - dx,y))

    for B in list(B_in_row):
        covered.remove(B)
    print(len(covered))

        


if __name__ == "__main__":
    run()
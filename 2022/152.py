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
    xmin, xmax = ymin, ymax = 0, 4000000

    for sx, sy, bx, by in connections:
        distances.append([(sx, sy), (bx, by), abs(bx-sx) + abs(by-sy)])

    for y in range(ymin, ymax+1):
        intervals = []
        for S, B, MD in distances:
            if abs(y - S[1]) > MD:
                continue
            dist = MD - abs(y - S[1])
            left, right = S[0] - dist, S[0] + dist
            intervals.append([max(xmin, left), min(xmax, right)])

        intervals.sort()
        
        idx = 1
        while idx < len(intervals):
            interval = intervals[idx]
            if interval[-1] <= intervals[idx-1][-1] + 1:
                intervals.pop(idx)
                continue
            
            if interval[0] > intervals[idx-1][-1] + 1:
                print(interval[0]-1, y)
                return
            idx += 1
        print(intervals, y)
        
                
        


if __name__ == "__main__":
    run()
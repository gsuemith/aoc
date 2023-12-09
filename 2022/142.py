def run():
    with open("14.txt", "r") as f:
        lines = f.readlines()

    paths = [[(int(x),int(y)) for x,y in [coords.split(",") for coords in line.strip().split(" -> ")]] for line in lines]

    bottom = max(max(coord[1] for coord in path) for path in paths) + 2
    maxx = 540#max(max(coord[0] for coord in path) for path in paths)
    minx = 450#min(min(coord[0] for coord in path) for path in paths)
    print(minx, maxx, bottom)
    # paths.append([(0, bottom), (maxx*3, bottom)])
    
    
    source = (500,0)

    blocked = set()

    for path in paths:
        for i, point in enumerate(path[:-1]):
            next = path[i+1]

            axis = 0 if point[0] != next[0] else 1
            rock = [*point]
            dir = -1 if next[axis] < point[axis] else 1

            for coord in range(point[axis], next[axis], dir):
                rock[axis] = coord
                blocked.add(tuple(rock))

        blocked.add(path[-1])

    


    
    total = 0
    stopped = set()
    loc = None
    while loc != source:
        loc = source
        down = (loc[0], loc[1] + 1)
        left = (loc[0] - 1, loc[1] + 1)
        right = (loc[0] + 1, loc[1] + 1)

        next = [down, left, right]
        while any(available(coord, blocked, stopped, bottom) for coord in next):
            for coord in next:
                if available(coord, blocked, stopped, bottom):
                    loc = coord
                    break
            if loc[1] == bottom:
                break

            down = (loc[0], loc[1] + 1)
            left = (loc[0] - 1, loc[1] + 1)
            right = (loc[0] + 1, loc[1] + 1)

            next = [down, left, right]
        
        stopped.add(loc)
        total += 1
        # print(total)
        # for i in range(120,bottom+3):
        #     line = ""
        #     for j in range(minx, maxx+1):
        #         line += "#" if (j, i) in blocked else "o" if (j,i) in stopped else "."

        #     print(line)
        # print("\n")

    print(total)
    for i in range(bottom+3):
        line = ""
        for j in range(420, 580):
            line += "#" if (j, i) in blocked else "o" if (j,i) in stopped else "."

        print(line)
        # print("\n")

def available(coord, blocked, stopped, floor):
    return coord not in blocked and coord not in stopped and coord[1] != floor




    



        

if __name__ == "__main__":
    run()
from copy import deepcopy

rocks = [
    {
        "rock": [
            [[2,0],[3,0],[4,0],[5,0]]
        ],
        "bottom": [(0,0),(0,1),(0,2),(0,3)],
        "top": [(0,0),(0,1),(0,2),(0,3)]
    },
    {
        "rock": [
            [None, [3,2], None],
            [[2,1],[3,1], [4,1]],
            [None, [3,0], None]
        ],
        "bottom": [(1,0),(2,1),(1,2)],
        "top": [(1,0),(0,1),(1,2)]
    },
    {
        "rock": [
            [None,  None, [4,2]],
            [None,  None, [4,1]],
            [[2,0], [3,0],[4,0]]
        ],
        "bottom": [(2,0),(2,1),(2,2)],
        "top": [(2,0),(2,1),(0,2)]
    },
    {
        "rock": [
            [[2,3]],[[2,2]],[[2,1]],[[2,0]]
        ],
        "bottom": [(3,0)],
        "top": [(0,0)]
    },
    {
        "rock": [
            [[2,1],[3,1]],
            [[2,0],[3,0]]
        ],
        "bottom": [(1,0),(1,1)],
        "top": [(0,0),(0,1)]
    }
]
push_axis = {">": 1, "<": -1}
swap = {">":"<", "<":">"}

def drop(rock, dy):
    for row in rock:
        for pos in row:
            if pos:
                pos[1] += dy

    return rock

def is_falling(rock, bottom, stopped):
    # print(len(stopped))
    # print([(rock[i][j][0], rock[i][j][1] - 1) not in stopped for i,j in bottom])
    # print(rock[-1])
    # print(tops)
    return all((rock[i][j][0], rock[i][j][1] - 1) not in stopped for i,j in bottom)


def puffed(rock, jet, stopped):
    dx = push_axis[jet]
    blocked = False
    # print(rock[-1])
    
    for row in rock:
        for pos in row:
            if pos:
                pos[0] += dx

                if pos[0] == 7 or pos[0] == -1 or tuple(pos) in stopped:
                    blocked = True

    # print(rock[-1])
    if blocked:
        return puffed(rock, swap[jet], stopped)
    return rock

def update_stopped(rock, stopped: set):
    for row in rock:
        for pos in row:
            if pos:
                stopped.add(tuple(pos))

def update_tops(tops: list, stopped: set):
    for x, y in list(stopped):
        tops[x] = max(y, tops[x])
    

if __name__ == "__main__":
    with open("17.txt", "r") as f:
        jets = f.readline().strip()

    puffs = len(jets)
    num_rocks = len(rocks)
    tops = [0]*7
    stopped = {(i,0) for i in range(7)}
    max_height = 0
    cycles = {}

    puff = 0
    for r in range(1899 + 2*1700 + 1):
        info = rocks[r%num_rocks]
        rock = deepcopy(info["rock"])
        bottom = info["bottom"]
        
        drop(rock, max_height+5)

        while is_falling(rock, bottom, stopped):
            drop(rock, -1)
            puffed(rock, jets[puff%puffs], stopped)
            puff += 1

        update_stopped(rock, stopped)
        update_tops(tops, stopped)
        max_height = max(tops)
        
        th = tuple([height - min(tops) for height in tops] + [r%num_rocks, puff%puffs])
        if th not in cycles:
            cycles[th] = []
        cycles[th].append((r,max_height))


        # print(tops)
        

    for th, rounds in cycles.items():
        if len(rounds) > 2:
            print(rounds)
            print([rounds[i][0] - rounds[i-1][0] for i in range(1, len(rounds))])
            print([rounds[i][1] - rounds[i-1][1] for i in range(1, len(rounds))])
            print(th, end="\n\n")
    print(max_height)
        


    
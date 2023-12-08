def run():
    with open("05.txt", "r") as f:
        lines = f.readlines()

    stacks_input = lines[:8]

    moves_input = [line.split() for line in lines[10:]]
    moves = [(int(move[1]), int(move[3]), int(move[5])) for move in moves_input]
    
    stacks = [[] for _ in range(10)]

    for line in stacks_input:
        for idx, char in enumerate(line):
            if char.isalpha():
                stacks[idx // 4 + 1].append(char)

    for stack in stacks:
        stack = stack.reverse()

    print(stacks[1][:-4:-1])
    print(stacks[1][:-3])

    for move, orig, dest in moves:
        stacks[0] = stacks[orig]
        stacks[dest] += stacks[0][:move*-1-1:-1]
        stacks[orig] = stacks[0][:move*-1]

    print("".join((stack[-1] if len(stack)>0 else " ") for stack in stacks[1:]))
    stacks[0] = []


    for stack in stacks:
        print(stack)


if __name__ == "__main__":
    run()
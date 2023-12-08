def run():
    with open("10.txt", "r") as f:
        data = f.readlines()

    commands = [line.split() for line in data]

    X = 1
    cycle = 0
    lines = []
    line = ""

    for cmd in commands:
        if cycle % 40 == 0:
                lines.append(line)
                line = ""


        line += "#" if cycle % 40 in {X-1,X,X+1} else "."

        if cmd[0] == 'noop':
            cycle += 1
        else:
            cycle += 1
            if cycle % 40 == 0:
                lines.append(line)
                line = ""
            line += "#" if cycle%40 in {X-1,X,X+1} else "."

            cycle += 1
        
       

        X += 0 if len(cmd) == 1 else int(cmd[1])
    lines.append(line)

    for x in lines:
        print(x)

if __name__ == "__main__":
    run()
def run():
    with open("10.txt", "r") as f:
        lines = f.readlines()

    commands = [line.split() for line in lines]

    X = 1
    cycle = 1
    signals = []
    for cmd in commands:
        if cycle % 40 == 20:
            signals.append((cycle, X))

        if cmd[0] == 'noop':
            cycle += 1
        else:
            cycle += 1
            if cycle % 40 == 20:
                signals.append((cycle, X))
            cycle += 1

        X += 0 if len(cmd) == 1 else int(cmd[1])

    print(signals[:5])
    signal_calc = [cycle * X for cycle, X in signals]
    print(signal_calc)
    print(sum(signal_calc))

if __name__ == "__main__":
    run()
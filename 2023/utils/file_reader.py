def read_file(filename="input.txt") -> list[str]:
    with open(filename, "r") as f:
        lines = f.readlines()

    return lines

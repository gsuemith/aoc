def run():
    with open("06.txt", "r") as f:
        line = f.readline()

    for idx in range(13, len(line)):
        char = line[idx]
        prev = set(list(line[idx-13:idx]))
        if len(prev) == 13 and char not in prev:
            print(idx, char, line[idx-13:idx+1])
            break

if __name__ == "__main__":
    run()
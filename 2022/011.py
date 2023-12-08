def run():
    with open("01.txt", "r") as f:
        lines = f.readlines()

    calories = [line.strip() for line in lines]

    most = 0
    current = 0

    for cal in calories:
        if cal:
            current += int(cal)
        else:
            most = max(most, current)
            current = 0

    print(most)

if __name__ == "__main__":
    run()
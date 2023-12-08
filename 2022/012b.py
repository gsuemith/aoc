def run():
    with open("01.txt", "r") as f:
        lines = f.readlines()

    calories = [line.strip() for line in lines]

    totals = []
    current = 0

    for cal in calories:
        if cal:
            current += int(cal)
        else:
            totals.append(current)
            current = 0

    totals.sort(reverse=True)
    print(totals[:3],sum(totals[:3]))

if __name__ == "__main__":
    run()
def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    histories = [[int(n) for n in line.split()] for line in lines]

    predictions = []

    for history in histories:
        diffs = history.copy()
        first = []

        while not all(diff == 0 for diff in diffs):
            new_diffs = []
            for i in range(1, len(diffs)):
                new_diffs.append(diffs[i]-diffs[i-1])

            first.append(diffs[0])
            diffs = new_diffs

        total = 0
        
        first.reverse()
        for n in first:
            total = n - total
        predictions.append(total)

    print(predictions)
    print(sum(predictions))
    

if __name__ == "__main__":
    run()
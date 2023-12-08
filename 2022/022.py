def run():
    with open("02.txt", "r") as f:
        lines = f.readlines()

    games = [line.split() for line in lines]

    result_scores = {"X": 0, "Y": 3, "Z": 6}
    move_points = {"X": 1, "Y": 2, "Z": 3}

    beats = {"A": "Y", "B": "Z", "C": "X"}
    as_theirs = {"A": "X", "B": "Y", "C": "Z"}

    beaten_by = {"A": "Z", "B": "X", "C": "Y"}

    total = 0

    for theirs, result in games:
        score = result_scores[result]
        if score == 6:
            score += move_points[beats[theirs]]
        elif score == 3:
            score += move_points[as_theirs[theirs]]
        else:
            score += move_points[beaten_by[theirs]]

        total += score

    print(total)


if __name__ == "__main__":
    run()
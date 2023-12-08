# def run():
#     with open("01.txt", "r") as f:
#         lines = f.readlines()


# if __name__ == "__main__":
#     run()

def run():
    with open("02.txt", "r") as f:
        lines = f.readlines()

    games = [line.split() for line in lines]

    move_points = {"X": 1, "Y": 2, "Z": 3}
    beats = {"A": "Y", "B": "Z", "C": "X"}
    as_theirs = {"X": "A", "Y": "B", "Z": "C"}

    total = 0

    for theirs, mine in games:
        score = move_points[mine]
        if mine == beats[theirs]:
            score += 6
        elif as_theirs[mine] == theirs:
            score += 3

        total += score

    print(total)


if __name__ == "__main__":
    run()
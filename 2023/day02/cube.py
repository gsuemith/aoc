limits = {"red": 12, "green": 13, "blue": 14}

def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    games = {}
    for line in lines:
        game, cubes = line.split(":")
        games[int(game[5:])] = [[(int(z.split(" ")[0]), z.split(" ")[1]) for z in hand.split(", ")] for hand in cubes.strip().split("; ")]
    
    total = 0
    for game_number, game in games.items():
        minimums = {}

        for hand in game:
            for number, color in hand:     
                minimums[color] = max(number, minimums[color]) if color in minimums else number

        power = 1
        for minimum in minimums.values():
            power *= minimum

        total += power


    print(total)


if __name__ == "__main__":
    run()
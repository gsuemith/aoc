def run():
    with open("03.txt", "r") as f:
        lines = f.readlines()

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorities = {c: idx + 1 for idx, c in enumerate(letters)}

    total = 0

    for group in range(len(lines)//3):
        i = group*3
        j = group*3 + 1
        k = group*3 + 2
        rucksack_1 = set(lines[i])
        rucksack_2 = set(lines[j])
        rucksack_3 = lines[k]
        badge = next(char for char in rucksack_3 if char in rucksack_1 and char in rucksack_2)
        total += priorities[badge]

    print(total)

if __name__ == "__main__":
    run()
def run():
    with open("03.txt", "r") as f:
        lines = f.readlines()

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorities = {c: idx + 1 for idx, c in enumerate(letters)}

    total = 0

    for rucksack in lines:
        size = len(rucksack) // 2
        comp_1 = set(rucksack[:size])
        print(comp_1)
        comp_2 = rucksack[size:]
        in_both = next((char for char in comp_2 if char in comp_1), "a")
        total += priorities[in_both]

    print(total)

if __name__ == "__main__":
    run()
def run():
    with open("04.txt", "r") as f:
        lines = f.readlines()

    assignments = [[tuple([int(n) for n in pair.split("-")]) for pair in line.strip().split(",")] for line in lines]
    count = 0
    for elf1, elf2 in assignments:
        if elf1[0] >= elf2[0] and elf1[1] <= elf2[1] or elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            count += 1

    print(count)

    

if __name__ == "__main__":
    run()
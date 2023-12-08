def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    rows = len(lines)
    cols = len(lines[0])

    total = 0
    ratios = []
    non_gear = {"a": 0}


    # for i in range(rows):
    #     number = ""
    #     is_part = False
    #     for j in range(cols):
    #         char = lines[i][j]
    #         if char.isdigit():
    #             number += char
    #             is_part = is_part or is_part_number(i, j, rows, cols, lines)
    #         else:
    #             if is_part:
    #                 total += int(number)
    #             number = ""
    #             is_part = False
    #     if is_part:
    #         total += int(number)
    for i in range(rows):
        for j in range(cols):
            char = lines[i][j]
            if char == "*" and is_gear(i, j, rows, cols, lines, non_gear):
                ratios.append(get_gear_ratio(i,j,rows,cols,lines))
    
    # print(rows, cols)
    # print(ratios)
    print(sum(ratios), len(ratios))

def get_gear_ratio(i,j,r,c,lines):
    numbers = set()
    for y in range(i-1, i+2):
    
        for x in range(j-1, j+2):
      
            if lines[y][x].isdigit():
                numbers.add(get_number(y,x,c,lines))
    
    numbers = list(numbers)

    if len(numbers) != 2:
        return numbers[0]**2

    print(numbers)
    return numbers[0] * numbers[1]

def get_number(i,x,c,lines):
    number = lines[i][x]

    j = x + 1
    while j < c and lines[i][j].isdigit():
        number += lines[i][j]
        j += 1

    j = x - 1
    while j >= 0 and lines[i][j].isdigit():
        number = lines[i][j] + number
        j -= 1

    return int(number)



def is_gear(i, j, r, c, lines: list[str], non_gear):
    adjacent_nums = 0
    if i-1 >= 0:
        y = i-1
        row = [lines[y][x].isdigit() for x in range(max(j-1,0), min(j+2,c))]
        if sum(row) == 2 and row[1] == False:
            adjacent_nums += 2
        elif sum(row) > 0:
            adjacent_nums += 1
    if i+1 < r:
        y = i+1
        row = [lines[y][x].isdigit() for x in range(max(j-1,0), min(j+2,c))]
        if sum(row) == 2 and row[1] == False:
            adjacent_nums += 2
        elif sum(row) > 0:
            adjacent_nums += 1

    adjacent_nums += sum([j>=1 and lines[i][j-1].isdigit(), j+1<c and lines[i][j+1].isdigit()])
    if adjacent_nums == 2:
        print()
        print("".join([lines[i-1][x] for x in range(j-1, j+2)]))
        print("".join([lines[i][x] for x in range(j-1, j+2)]))
        print("".join([lines[i+1][x] for x in range(j-1, j+2)]))
        print()

    return adjacent_nums == 2

def is_symbol(char: str):
    return not char.isdigit() and char != "."

def is_part_number(i, j, rows, cols, lines):
    adjacent_symbol = False
    for x in range(j-1, j+2):
        if x < 0 or x >= cols:
            continue
        for y in range(i-1, i+2):
            if y < 0 or y >= rows or (j == x and i == y):
                continue
            adjacent_symbol = adjacent_symbol or is_symbol(lines[y][x])

    return adjacent_symbol


if __name__ == "__main__":
    run()
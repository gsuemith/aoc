def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    data = [line.strip().split() for line in lines]
    rows = [[row[0], [int(n) for n in row[1].split(",")]] for row in data]
    grouping_intervals = []

    for conditions, groupings in rows:
        start = 0
        intervals = []
        for grouping in groupings:
            intervals.append((start, start+grouping))
            start += grouping + 1

        grouping_intervals.append([conditions, intervals])
    # print(grouping_intervals[4:5])

    possibilities = []
    for conditions, intervals in grouping_intervals[:]:
        print()
        print(intervals)
        print("".join(f"  {char}" for char in conditions))
        print("".join(f"{n:3}" for n in range(len(conditions))))
        end_combos = {len(conditions): 1 }
        print(end_combos)
        end_limit = len(conditions)

        while len(intervals) > 0:
            interval = intervals.pop()
            
            start, end = interval
            valid_starts = []
            invalid_ends = set()
            while end <= end_limit:
                if (
                    all(char != "." for char in conditions[start:end]) and
                    (start == 0 or conditions[start-1] != "#") and
                    (end == len(conditions) or conditions[end] != "#")
                ):
                    valid_starts.append((start, end))
                else:
                    invalid_ends.add(end)
             
                    
                start += 1
                end += 1

            end_combos = {start-1: sum(combos for valid_end, combos in end_combos.items() 
                                       if valid_end >= end and "#" not in set(conditions[end: valid_end])) 
                                       for start, end in valid_starts}
            end_limit = valid_starts[-1][0] - 1
            print(end_combos)

            

        combos = sum(combo for end, combo in end_combos.items() if end < 0 or "#" not in set(conditions[:end]))
        print(combos)
        possibilities.append(combos)
    
    print(sum(possibilities))


if __name__ == "__main__":
    run()
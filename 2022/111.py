def run():
    with open("11.txt", "r") as f:
        lines = f.readlines()

    monkeys = []
    for i in range(len(lines) // 7 + 1):
        monkey = {}
        monkey["items"] = [int(x) for x in lines[i*7 + 1].strip().split(": ").pop().split(", ")]
        monkey["op"] = lines[i*7 + 2].split("=")[1].split()
        monkey["div"] = int(lines[i*7 + 3].split().pop())
        if_true = int(lines[i*7 + 4].split().pop())
        if_false = int(lines[i*7 + 5].split().pop())
        monkey["next"] = (if_false, if_true)
        monkey["inspections"] = 0

        monkeys.append(monkey)

    print(len(monkeys))
    for round in range(20):
        for monkey in monkeys:
            monkey["inspections"] += len(monkey["items"])
            while len(monkey["items"]) > 0:
                item = monkey["items"].pop()
                op = monkey["op"]
                op2 = item if op[2] == "old" else int(op[2])

                new = item * op2 if op[1] == "*" else item + op2
                next = monkey["next"][new // 3 % monkey["div"] == 0]
                # print(item, op, new)
                monkeys[next]["items"].append(item)
        print([x["inspections"] for x in monkeys])

    inspections = [x["inspections"] for x in monkeys]
    inspections.sort()
    print(inspections[-1]* inspections[-2])




if __name__ == "__main__":
    run()
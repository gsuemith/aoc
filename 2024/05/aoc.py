from collections import defaultdict

def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    data = [line.strip() for line in lines]
    break_idx = 0
    for idx, line in enumerate(data):
        if line == "":
            break_idx = idx
            break
    graph = defaultdict(set)
    for idx in range(break_idx):
        a,b = data[idx].split("|")
        graph[b].add(a)

    total = 0
    for idx in range(break_idx+1,len(data)):
        pages = data[idx].split(",")

        printed = set()
        valid = True
        for i in range(len(pages)):
            for j in range(i+1, len(pages)):
                if pages[i] not in graph[pages[j]]:
                    valid = False
                    pages[i], pages[j] = pages[j], pages[i]

        print(valid, " : ", pages)
        if not valid:
            total += int(pages[len(pages) // 2])

    print(total)


def print_page(page, printed, graph):

    if page not in graph or len(printed) == 0:
        return True
    dependencies = graph[page]

    return any(page in dependencies for page in printed)


if __name__ == "__main__":
    run()
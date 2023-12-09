def run():
    with open("13.txt", "r") as f:
        lines = f.readlines()

    pairs = []
    for i in range(len(lines) // 3 + 1):
        pairs.append([lines[i*3].strip(), lines[i*3+1].strip()])

    # for i in range(len(pairs)):
    #     print(pairs[i])
    # print()

    for pair in pairs:
        pair[0], pair[1] = to_list(pair[0]), to_list(pair[1])
    

    # for i in range(len(pairs)):
    #     print(pairs[i])
    # print(pairs[6])

    indices = []
    for i in range(len(pairs)):
        a, b = pairs[i]
        if compare(a, b) <= 0:
            indices.append(i+1)

    print(indices)
    print(sum(indices))


def compare(a: list, b: list):
    if all(type(item) is int for item in a) and all(type(item) is int for item in b):
        return (0,-1)[a<b] if a <= b else 1

    for i in range(min(len(a), len(b))):
        a_i, b_i = a[i], b[i]

        if type(a_i) is not type(b_i):
            comparison = compare([a_i], b_i) if type(a_i) is int else compare(a_i, [b_i])
            if comparison == 0:
                continue
            return comparison
        elif type(a_i) is int:
            if a_i == b_i:
                continue
            return (1,-1)[a_i < b_i]
        else:
            comparison = compare(a_i, b_i)
            if comparison == 0:
                continue
            return comparison
        
    return (0,-1)[len(a) < len(b)] if len(a) <= len(b) else 1



def to_list(str_list: str):
    # print(str_list)
    if str_list == "[]":
        return []
    
    final_list = []
    inside = str_list[1:-1]

    i = 0
    item = ""
    while i < len(inside):
        char = inside[i]
        if char =='[':
            item = char
            stack = 1
            while stack > 0:
                i += 1
                char = inside[i]
                item += char
                if char == ']':
                    stack -= 1
                elif char == '[':
                    stack += 1
            item = to_list(item)

        elif char == ',':
            final_list.append(int(item) if not type(item) is list else item)
            item = ""

        else:
            item += char

        i += 1
    
    if item or item == []:
        final_list.append(int(item) if not type(item) is list else item)

    
    return final_list

        
                


    

if __name__ == "__main__":
    run()
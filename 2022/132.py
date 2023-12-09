from functools import cmp_to_key

def run():
    with open("13.txt", "r") as f:
        lines = f.readlines()

    packets = []
    for i in range(len(lines) // 3 + 1):
        packets.append(to_list(lines[i*3].strip()))
        packets.append(to_list(lines[i*3+1].strip()))

    packets.sort(key=cmp_to_key(compare))


    dps = [find([[2]], packets) + 1, find([[6]], packets) + 1]
    print(dps)
    # dps = []

    # for idx, packet in enumerate(packets):
    #     if packet == [[2]] or packet == [[6]]:
    #         dps.append(idx+1)

    print(dps[1]*dps[0])

def find(key, packets):
    left = 0
    right = len(packets) - 1
    mid = (left + right) // 2

    while left < right:
        if packets[mid] == key:
            return mid
        comparison = compare(key, packets[mid])
        if comparison < 0:
            right = mid
        else:
            left = mid
        mid = (left + right) // 2



    return -1



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
def run():
    with open("input.txt", "r") as f:
        sequence = f.readlines().pop().strip().split(",")

    sequence = [split(s) for s in sequence]

    boxes = [{} for _ in range(256)]
    
    for label, op, box_idx in sequence:
        box = boxes[box_idx]
        if op == "-":
            if label in box:
                pos = box[label][0]
                del box[label]
                for lens in box.values():
                    if lens[0] > pos:
                        lens[0] -= 1

        else:
            pos = len(box) + 1 if label not in box else box[label][0]
                
            box[label] = [pos, op]

    total = 0
    for idx, box in enumerate(boxes):
        for label, lens in box.items():
            total += (idx+1)*lens[0]*lens[1]

    print(total)

def hash(s):
    total = 0
    for c in s:
        total += ord(c)
        total *= 17
        total %= 256
    return total

def split(s):
    if s[-1] == "-":
        return (s[:-1], s[-1], hash(s[:-1]))
    seq, n = s.split("=")
    return (seq, int(n), hash(seq))



if __name__ == "__main__":
    run()
def dicho(seq, up, down):
    total = 2 ** len(seq)
    offset = total // 2 if seq.pop(0) == up else 0
    if total == 2:
        return offset
    return offset + dicho(seq, up, down)

def make_ids(lines):
    ids = []
    for line in lines:
        row = dicho(list(line[:7]), 'B', 'F')
        seat = dicho(list(line[7:-1]), 'R', 'L')
        ids.append(row * 8 + seat)
    return ids


def find_my_id(ids):
    ids = sorted(ids)
    for i, seat in enumerate(ids):
        if (ids[i+1] - seat) == 2:
            return seat + 1

if __name__ == "__main__":
    with open("inputs/day05.txt", "r") as f:
        lines = list(f)
    ids = make_ids(lines)
    print("Part 1:", max(ids))
    print("Part 2:", find_my_id(ids))

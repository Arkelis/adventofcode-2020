import re


def apply_mask(val, mask):
    val = format(int(val), "#038b")[2:]
    for i, char in enumerate(mask):
        if char == "X":
            continue
        val = val[:i] + char + val[i+1:]
    return int(val, 2)


def addresses_generator(address):
    n_of_x = address.count("X")
    for n in range(2**n_of_x):
        bin_n = format(n, f"#0{n_of_x+2}b")[2:]
        address_copy = str(address)
        for char in bin_n:
            address_copy = address_copy.replace("X", char, 1)
        yield int(address_copy, 2)


def get_all_addresses(address, mask):
    address = format(int(address), "#038b")[2:]
    for i, char in enumerate(mask):
        if char == "0":
            continue
        address = address[:i] + char + address[i+1:]
    return addresses_generator(address)


def process_lines(lines, part):
    mems = {}
    mask = "" * 36
    for line in lines:
        if line.startswith("mask"):
            mask = line.rstrip().split(" = ")[1]
            continue
        match = re.search(r"mem\[(\d+)\] = (\d+)", line)
        address = int(match.group(1))
        val = int(match.group(2))
        if part == 1:
            mems[address] = apply_mask(val, mask)
        elif part == 2:
            mems.update({address: val for address in get_all_addresses(address, mask)})
    return mems

if __name__ == "__main__":
    with open("inputs/day14.txt", "r") as f:
        lines = list(f)
    print("Part 1:", sum(process_lines(lines, 1).values()))
    print("Part 2:", sum(process_lines(lines, 2).values()))

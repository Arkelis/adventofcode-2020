import re


def get_sum(lines):
    def compute_line(line):
        while parenthised_groups := re.findall(r"\(([0-9 *+]+)?\)", line):
            for g in parenthised_groups:
                line = line.replace(f"({g})", str(compute_line(g)))
        n, op = int(line.split(" ")[0]), ""
        for el in line.split(" ")[1:]:
            try:
                n = n + int(el) if op == "+" else n * int(el)
            except ValueError:
                op = el
        return n 

    return sum(map(compute_line, lines))


def get_sum_part_two(lines):
    def compute_line(line):
        while parenthised_groups := re.findall(r"\(([0-9 *+]+)?\)", line):
            for g in parenthised_groups:
                line = line.replace(f"({g})", str(compute_line(g)))
        s = 1
        for sub in line.split(" * "):
            s *= sum(map(int, sub.split(" + ")))
        return s

    return sum(map(compute_line, lines))


if __name__ == "__main__":
    with open("inputs/day18.txt", "r") as f:
        lines = list(f)
    print("Part 1:", get_sum(lines))
    print("Part 1:", get_sum_part_two(lines))

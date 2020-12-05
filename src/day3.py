def count_trees(slope_right, slope_bottom, lines):
    x = 0
    trees = 0
    pattern_width = len(lines[0]) - 1
    for y in range(0, len(lines), slope_bottom):
        trees += lines[y][x%pattern_width] == "#"
        x += slope_right
    return trees

if __name__ == "__main__":
    with open("inputs/day3.txt", "r") as f:
        lines = list(f)

    print("Part 1", count_trees(3, 1, lines))
    print("Part 2", (
        count_trees(3, 1, lines)
        * count_trees(1, 1, lines)
        * count_trees(7, 1, lines)
        * count_trees(5, 1, lines)
        * count_trees(1, 2, lines)
    ))

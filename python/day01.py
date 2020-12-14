def find_complementary(total, n, numbers):
    compl = total - n
    if compl in numbers:
        return compl
    return False

if __name__ == "__main__":
    # Part 1
    with open("inputs/day01.txt", "r") as f:
        numbers = list(map(int, f))

    for n in numbers:
        compl = find_complementary(2020, n, numbers)
        if compl:
            print("Part 1", compl * n)
            break

    # Part 2
    break_ = False
    for n in numbers:
        if break_:
            break
        for m in numbers:
            compl = find_complementary(2020, n+m, numbers)
            if compl:
                print("Part 2", compl * n * m)
                break_ = True
                break

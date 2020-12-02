def find_complementary(total, n, numbers):
    """Find total - n in numbers list.
    
    Return result if founded, else False.
    """
    to_find = total - n
    if to_find in numbers:
        return to_find
    else:
        return False

# Part 1
with open("inputs/day1.txt", "r") as f:
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
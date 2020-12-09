from collections import deque


def find_first_wrong(preamble, numbers):
    previous_numbers = deque(preamble, maxlen=25)
    sums = {n + m for n in previous_numbers for m in previous_numbers if n != m}
    for n in numbers:
        if n not in sums:
            return n
        previous_numbers.append(n)
        sums = {n + m for n in previous_numbers for m in previous_numbers if n != m}


def find_contigous_sum_for(number, numbers):
    contigous_sum = 0
    sum_numbers = []
    for current in numbers:
        if contigous_sum == number:
            break
        contigous_sum += current
        sum_numbers.append(current)
        while contigous_sum > number:
            contigous_sum -= sum_numbers.pop(0)
    return min(sum_numbers) + max(sum_numbers)


if __name__ == "__main__":
    with open("inputs/day9.txt", "r") as f:
        lines = list(f)
    preamble, numbers = tuple(map(int, lines[:25])), tuple(map(int, lines[25:]))
    first_wrong = find_first_wrong(preamble, numbers)
    print("Part 1:", first_wrong)
    print("Part 2:", find_contigous_sum_for(first_wrong, [*preamble, *numbers]))

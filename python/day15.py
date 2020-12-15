from collections import deque


def find_number_of_turn(turn, init_numbers):
    mem = {n: i for i, n in enumerate(init_numbers[:-1], 1)}
    last_number = init_numbers[-1]
    for i in range(len(init_numbers), turn):
        current_number = (
            i - mem[last_number]
            if mem.get(last_number) is not None
            else 0
        )
        mem[last_number] = i
        last_number = current_number
    return last_number


if __name__ == "__main__":
    with open("inputs/day15.txt", "r") as f:
        numbers = list(map(int, f.readline().split(",")))
    print("Part 1:", find_number_of_turn(2020, numbers))
    print("Part 2:", find_number_of_turn(30000000, numbers))
from collections import deque


# submited with this, but takes a lot of memory for part 2
# todo: optimize for large number of turns
def find_number_of_turn(turn, init_numbers):
    mem = {n: deque([i], maxlen=2) for i, n in enumerate(init_numbers, 1)}
    last_number = init_numbers[-1]
    for i in range(len(init_numbers)+1, turn+1):
        last_number = (
            mem[last_number][0] - mem[last_number][1]
            if len(mem[last_number]) == 2
            else 0
        )
        mem.setdefault(last_number, deque([], maxlen=2)).appendleft(i)
    return last_number


if __name__ == "__main__":
    with open("inputs/day15.txt", "r") as f:
        numbers = list(map(int, f.readline().split(",")))
    print("Part 1:", find_number_of_turn(2020, numbers))
    print("Part 2:", find_number_of_turn(30000000, numbers))
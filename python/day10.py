import math
import functools


def find_differences(joltages):
    joltages = sorted(set(joltages))
    diffs = dict(((i, 0) for i in range(1, 4)))
    last = len(joltages) - 1
    diffs[joltages[0]] += 1
    for i, joltage in enumerate(joltages):
        if i == last:
            diffs[3] += 1
            break
        diffs[joltages[i+1]-joltage] += 1
    return diffs


def find_arrangements_count(joltages):
    """Find arrangements count for reaching device joltage

    To do this, count for each adapter the numbers of ways to reach them.

    Example: Let nX the number of ways to reach X.
    Given 1 4 5 6 7 10 11 12 15 16 19 adapters:

    0 -> 1    1 way to reach 1: n1 = 1

    1 -> 4    n4 = 1

    4 -> 5    n5 = 1
      -> 6    n6 = 1
      -> 7    n7 = 1

    5 -> 6    2nd way to reach 6 => n6 = 2
      -> 7    2nd way to reach 7 => n7 = 2 

    6 -> 7    3rd way to reach 7 => n7 = n7 + n6 = 4

    7 -> 10   we reach only 10 through 7. Because n7 = 4, then n10 = 4

    10 -> 11  n10 = 4 => n11 = 4   
       -> 12  n10 = 4 => n12 = 4

    11 -> 12  n11 = 4 => n12 = n12 + n11 = 8

    12 -> 15  n12 = 8 => n15 = 8

    15 -> 16  n15 = 8 => n16 = 8

    So n22 = 8.

    Generally, for given X, nX = n(X-1) + n(X-2) + n(X-3)
    """
    n_ways_to_reach = {0: 1}
    device_joltage = max(joltages) + 3
    for joltage in joltages + (device_joltage,):
        n_ways_to_reach[joltage] = (
            n_ways_to_reach.get(joltage - 1, 0)
            + n_ways_to_reach.get(joltage - 2, 0)
            + n_ways_to_reach.get(joltage - 3, 0)
        )
    return n_ways_to_reach[device_joltage]

if __name__ == "__main__":
    with open("inputs/day10.txt", "r") as f:
        joltages = list(map(int, f))
    diffs = find_differences(joltages)
    print("Part 1:", diffs[1] * diffs[3])
    print("Part 2:", find_arrangements_count(tuple(sorted(set(joltages)))))

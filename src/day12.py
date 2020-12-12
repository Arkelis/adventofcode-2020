handle_part_one = {
    "N": lambda v, n, e, t: (n+v, e, t),
    "S": lambda v, n, e, t: (n-v, e, t),
    "E": lambda v, n, e, t: (n, e+v, t),
    "W": lambda v, n, e, t: (n, e-v, t),
    "L": lambda v, n, e, t: (n, e, (t-v)%360),
    "R": lambda v, n, e, t: (n, e, (t+v)%360),
    "F": lambda v, n, e, t: (
        (n+v, e, t) if t == 0
        else (n, e+v, t) if t == 90
        else (n-v, e, t) if t == 180
        else (n, e-v, t) if t == 270
        else None
    ),
}


def navigate_part_one(instructions):
    n, e = 0, 0 # north and east positions
    target = 90 # number of degres (0=north, 180=south)
    for action, value in instructions:
        n, e, target = handle_part_one[action](value, n, e, target)
    return abs(n) + abs(e)


handle_part_two = {
    "N": lambda v, n, e, tn, te: (n, e, tn+v, te),
    "S": lambda v, n, e, tn, te: (n, e, tn-v, te),
    "E": lambda v, n, e, tn, te: (n, e, tn, te+v),
    "W": lambda v, n, e, tn, te: (n, e, tn, te-v),
    "L": lambda v, n, e, tn, te: (
        (n, e, te, -tn) if v == 90
        else (n, e, -tn, -te) if v == 180
        else (n, e, -te, tn) if v == 270
        else None
    ),
    "R": lambda v, n, e, tn, te: handle_part_two["L"](-v%360, n, e, tn, te),
    "F": lambda v, n, e, tn, te: (n+tn*v, e+te*v, tn, te),
}


def navigate_part_two(instructions):
    n, e = 0, 0 # north and east positions
    target = (1, 10) # n, e of waypoint
    for action, value in instructions:
        n, e, *target = handle_part_two[action](value, n, e, *target)
    return abs(n) + abs(e)


if __name__ == "__main__":
    with open("inputs/day12.txt", "r") as f:
        instructions = list(f)
    instructions = tuple((i[0], int(i[1:])) for i in instructions)
    print("Part 1:", navigate_part_one(instructions))
    print("Part 2:", navigate_part_two(instructions))

rules_part_one = {
    "#": lambda next_seats: "L" if next_seats.count("#") >= 4 else "#",
    "L": lambda next_seats: "#" if "#" not in next_seats else "L",
}

rules_part_two = {
    "#": lambda visible_seats: "L" if visible_seats.count("#") >= 5 else "#",
    "L": lambda visible_seats: "#" if "#" not in visible_seats else "L",
}


def find_next_seats(x, y, seats_map):
    return {
        (xx, yy)
        for xx in {max(0, x-1), x, min(x+1, len(seats_map[0])-1)}
        for yy in {max(0, y-1), y, min(y+1, len(seats_map)-1)}
        if (xx, yy) != (x, y)
    }


def bound_with_map(func, seats_map):
    def wrapped(x, y):
        new_x, new_y = func(x, y)
        bound_x = max(0, min(new_x, len(seats_map[0])-1))
        bound_y = max(0, min(new_y, len(seats_map)-1))
        if bound_x != new_x or bound_y != new_y:
            return (-1, -1)
        return new_x, new_y
    return wrapped


def find_visible_seats(x, y, seats_map):
    visible_seats = set()
    for op in (
        bound_with_map(lambda x, y: (x, y+1), seats_map),
        bound_with_map(lambda x, y: (x, y-1), seats_map),
        bound_with_map(lambda x, y: (x+1, y), seats_map),
        bound_with_map(lambda x, y: (x-1, y), seats_map),
        bound_with_map(lambda x, y: (x+1, y+1), seats_map),
        bound_with_map(lambda x, y: (x-1, y-1), seats_map),
        bound_with_map(lambda x, y: (x-1, y+1), seats_map),
        bound_with_map(lambda x, y: (x+1, y-1), seats_map),
    ):
        visible_seat = "."
        old_x, old_y = x, y
        while visible_seat == ".":
            new_x, new_y = op(old_x, old_y)
            if (new_x, new_y) == (-1, -1):
                new_x, new_y = old_x, old_y
                break
            visible_seat = seats_map[new_y][new_x]
            old_x, old_y = new_x, new_y
        if (new_x, new_y) == (x, y) or visible_seat == ".":
            continue
        visible_seats.add((new_x, new_y))
    # if (x, y) == (3, 8): input()
    return visible_seats


def get_next_state(x, y, seats_map, seats_to_check_for, rules):
    current_state = seats_map[y][x]
    if current_state == ".":
        return current_state
    states_to_check = [seats_map[y][x] for x, y in seats_to_check_for[(x, y)]]
    return rules[current_state](states_to_check)


def get_next_map(seats_map, seats_to_check_for, rules):
    return [
        [
            get_next_state(x, y, seats_map, seats_to_check_for, rules) if seats_map[y][x] != "." else "."
            for x in range(len(seats_map[0]))
        ]
        for y in range(len(seats_map))
    ]


def get_stable_map(seats_map, seats_to_check_factory=find_next_seats, rules=rules_part_one):
    seats_to_check_for = {(x, y): seats_to_check_factory(x, y, seats_map)
        for x in range(len(seats_map[0]))
        for y in range(len(seats_map))
    }
    new_seats_map = get_next_map(seats_map, seats_to_check_for, rules)
    while new_seats_map != seats_map:
        seats_map = new_seats_map
        new_seats_map = get_next_map(seats_map, seats_to_check_for, rules)
    return new_seats_map


if __name__ == "__main__":
    with open("inputs/day11.txt", "r") as f:
        seats_map = [list(line)[:-1] for line in f]
    print("Part 1:", sum(char == "#" for line in get_stable_map(seats_map) for char in line))
    print("Part 2:", sum(char == "#" for line in get_stable_map(seats_map, find_visible_seats, rules_part_two) for char in line))



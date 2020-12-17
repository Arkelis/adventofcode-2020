# we could have used numpy
# instead, we only use standard library
import functools


def get_neighbors_coordinates(x, y, z, world_size):
    return set(
        (a, b, c)
        for a in range(max(0, x-1), min(world_size-1, x+1)+1)
        for b in range(max(0, y-1), min(world_size-1, y+1)+1)
        for c in range(max(0, z-1), min(world_size-1, z+1)+1)
        if (a, b, c) != (x, y, z)
    )


def get_next_cell_state(x, y, z, world, world_size):
    current_state = world[z][y][x]
    values = tuple(world[c][b][a] for (a, b, c) in get_neighbors_coordinates(x, y, z, world_size))
    return {
        "#": "#" if 2 <= len(list(filter(lambda x: x == "#", values))) <= 3 else ".",
        ".": "#" if len(list(filter(lambda x: x == "#", values))) == 3 else ".",
    }[current_state]


def get_next_state(world, world_size):
    return tuple(tuple(tuple(get_next_cell_state(x, y, z, world, world_size) 
               for x in range(world_size))
               for y in range(world_size))
               for z in range(world_size))


def get_world_after(cycles, init_state):
    world_size = len(init_state) + cycles*2
    world = [[["." for _ in range(world_size)] for _ in range(world_size)] for _ in range(world_size)]
    for x in range(len(init_state)):
        for y in range(len(init_state)):
            world[cycles+1][cycles+y][cycles+x] = init_state[y][x]
    world = tuple(tuple(tuple(world[z][y][x] 
               for x in range(world_size))
               for y in range(world_size))
               for z in range(world_size))
    for _ in range(cycles):
        world = get_next_state(world, world_size)
    return world


def get_active_count(world):
    return sum(sum(sum(map(lambda x: 1 if x == "#" else 0, world[z][y])) for y in range(len(world))) for z in range(len(world)))


def hyper_get_neighbors_coordinates(x, y, z, w, world_size):
    return set(
        (a, b, c, d)
        for a in range(max(0, x-1), min(world_size-1, x+1)+1)
        for b in range(max(0, y-1), min(world_size-1, y+1)+1)
        for c in range(max(0, z-1), min(world_size-1, z+1)+1)
        for d in range(max(0, w-1), min(world_size-1, w+1)+1)
        if (a, b, c, d) != (x, y, z, w)
    )


def hyper_get_next_cell_state(x, y, z, w, world, world_size):
    current_state = world[w][z][y][x]
    values = tuple(world[d][c][b][a] for (a, b, c, d) in hyper_get_neighbors_coordinates(x, y, z, w, world_size))
    return {
        "#": "#" if 2 <= len(list(filter(lambda x: x == "#", values))) <= 3 else ".",
        ".": "#" if len(list(filter(lambda x: x == "#", values))) == 3 else ".",
    }[current_state]


def hyper_get_next_state(world, world_size):
    return tuple(tuple(tuple(tuple(hyper_get_next_cell_state(x, y, z, w, world, world_size) 
                             for x in range(world_size))
                             for y in range(world_size))
                             for z in range(world_size))
                             for w in range(world_size))


def hyper_get_world_after(cycles, init_state):
    world_size = len(init_state) + cycles*2
    world = [[[["." for _ in range(world_size)] for _ in range(world_size)] for _ in range(world_size)] for _ in range(world_size)]
    for x in range(len(init_state)):
        for y in range(len(init_state)):
            world[cycles+1][cycles+1][cycles+y][cycles+x] = init_state[y][x]
    world = tuple(tuple(tuple(tuple(world[w][z][y][x] 
                              for x in range(world_size))
                              for y in range(world_size))
                              for z in range(world_size))
                              for w in range(world_size))
    for _ in range(cycles):
        world = hyper_get_next_state(world, world_size)
    return world


def hyper_get_active_count(world):
    return sum(sum(sum(sum(map(lambda x: 1 if x == "#" else 0, world[w][z][y])) for y in range(len(world))) for z in range(len(world))) for w in range(len(world)))


if __name__ == "__main__":
    with open("inputs/day17.txt", "r") as f:
        init_state = [list(line)[:-1] for line in f]
    print("Part 1:", get_active_count(get_world_after(6, init_state)))
    print("Part 2:", hyper_get_active_count(hyper_get_world_after(6, init_state)))
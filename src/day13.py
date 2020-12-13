import operator
import functools
import math

def find_earliest_bus(earliest_timestamp, bus_ids):
    return min((
        (bus_id, earliest_timestamp - earliest_timestamp%bus_id + bus_id)
        for bus_id in bus_ids
    ), key=operator.itemgetter(1))


def find_first_sequence(bus_ids):
    # for this problem, we use Chinese remainder theorem algorithm
    # see https://math.stackexchange.com/questions/149709/hcf-lcm-and-remainders
    # and https://fr.wikipedia.org/wiki/Théorème_des_restes_chinois#Algorithme (French)
    prod = functools.reduce(lambda x, y: x * y, (int(x) for x in bus_ids if x != "x"))
    congrs = [(-i%bus_id, bus_id) for i, bus_id in enumerate(bus_ids) if bus_id != "x"]
    e_sum = 0
    for remainder, div in congrs:
        n_hat = prod // div
        e = n_hat
        while e % div != 1:
            e += n_hat
        e_sum += e * remainder
    # e_sum is a solution, but not the smallest.
    # to get the smallest solution, get the remainder by the product
    return e_sum % prod


if __name__ == "__main__":
    with open("inputs/day13.txt", "r") as f:
        lines = list(f)
        earliest_timestamp = int(lines[0])
        bus_ids = [int(bus_id) for bus_id in lines[1].split(",") if bus_id != "x"]
        bus_ids_with_x = [int(bus_id) if bus_id != "x" else "x" for bus_id in lines[1].split(",")]
    bus_id, earliest_departure = find_earliest_bus(earliest_timestamp, bus_ids)
    print("Part 1:", bus_id * (earliest_departure - earliest_timestamp))
    print("Part 2:", find_first_sequence(bus_ids_with_x))

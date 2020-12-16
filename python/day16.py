import re
import functools
import contextlib


def make_predicates_from_rules(rules):
    def make_predicate(rule):
        return lambda n: any(a <= n <= b for a, b in rule)
    predicates = {}
    for rule in rules:
        name, ranges = rule.split(": ")
        ranges = ranges.split(" or ")
        ranges = [tuple(map(int, n_range.split("-"))) for n_range in ranges]
        predicates[name] = make_predicate(ranges)
    return predicates


def find_invalid(nearby_tickets, predicates):
    n_invalid = sum(
        n if not any(predicate(n) for predicate in predicates.values()) else 0
        for ticket in nearby_tickets
        for n in map(int, ticket.split(","))
    )
    return n_invalid


def find_fields(nearby_tickets, predicates):
    def find_invalid_tickets(nearby_tickets, predicates):
        invalid_tickets = set(
            i if not any(predicate(n) for predicate in predicates.values()) else 0
            for i, ticket in enumerate(nearby_tickets)
            for n in map(int, ticket.split(","))
        )
        return invalid_tickets
    invalid_indexes = find_invalid_tickets(nearby_tickets, predicates)
    fields = [list(predicates.keys()) for _ in range(len(nearby_tickets[0].split(",")))]
    for index, ticket in filter(lambda x: x[0] not in invalid_indexes, enumerate(nearby_tickets)):
        if all(len(l) == 1 for l in fields):
            break
        for i, field in enumerate(map(int, ticket.split(","))):
            for rule, predicate in filter(lambda x: x[0] in fields[i], predicates.items()):
                if not predicate(field):
                    fields[i].remove(rule)
    while not all(len(l) == 1 for l in fields):
        for l in filter(lambda x: len(x) == 1, fields):
            for m in filter(lambda x: len(x) > 1, fields):
                with contextlib.suppress(ValueError):
                    m.remove(l[0])
    return [l[0] for l in fields]


if __name__ == "__main__":
    with open("inputs/day16.txt", "r") as f:
        blocks = map(lambda x: x.split("\n"), "".join(list(f)).split("\n\n"))
        rules = next(blocks)
        my_ticket = map(int, next(blocks)[1].split(","))
        nearby_tickets = next(blocks)[1:-1]
    print("Part 1:", find_invalid(nearby_tickets, make_predicates_from_rules(rules)))
    fields = find_fields(nearby_tickets, make_predicates_from_rules(rules))
    my_ticket = dict(zip(fields, my_ticket))
    print("Part 2:", functools.reduce(
        lambda x, y: x * y, 
        (val if rule.startswith("departure") else 1 for (rule, val) in my_ticket.items()))
    )
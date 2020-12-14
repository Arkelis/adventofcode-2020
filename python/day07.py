import re


def find_bags_containing(to_find, lines):
    containers = set()
    for line in lines:
        if to_find in line and not line.startswith(to_find):
            found = line.split("bags")[0][:-1]
            containers |= {found} | find_bags_containing(found, lines)
    return containers


def find_number_of_bags_in(container, lines):
    bags = 0
    for line in lines:
        if not line.startswith(container):
            continue
        # regex to find bags inside a container
        regex = (
            r"(\d+)"       # group 1: one or more digits (number of bags)
            r" ((\w+ ?)+)" # group 2: one or more groups of letters with eventually a trailing space (words) 
            r" bags?"      # the word bag, eventually plural
        )
        for match in re.finditer(regex, line): 
            bags += int(match.group(1)) * (1 + find_number_of_bags_in(match.group(2), lines))
            # the "1 +" stands for the actual containing bag we just found.
    return bags


if __name__ == "__main__":
    with open("inputs/day07.txt", "r") as f:
        lines = list(f)
    print("Part 1:", len(find_bags_containing("shiny gold", lines)))
    print("Part 2:", find_number_of_bags_in("shiny gold", lines))

def count_yes(possible_answers, group_answers, need_all=False):
	if need_all:
		group_answers = set.intersection(*map(set, group_answers.split(" ")))
	return sum(q in group_answers for q in possible_answers)


if __name__ == "__main__":
    with open("inputs/day06.txt", "r") as f:
        lines = (f.read() + "\n").replace("\n", " ").split("  ") # one line per group
    print("Part 1:", sum(count_yes("abcdefghijklmnopqrstuvwxyz", line) for line in lines))
    print("Part 2:", sum(count_yes("abcdefghijklmnopqrstuvwxyz", line, True) for line in lines))

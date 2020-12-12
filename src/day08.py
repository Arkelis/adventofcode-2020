def compute_acc(lines):
	last = len(lines) - 1
	visited = set()
	instruction_index = 0
	acc = 0
	while instruction_index not in visited:
		if instruction_index > last:
			break
		visited.add(instruction_index)
		inst, val = lines[instruction_index].split(" ")
		val = int(val)
		if inst == "acc":
			acc += val
			instruction_index += 1
		elif inst == "jmp":
			instruction_index += val
		elif inst == "nop":
			instruction_index += 1
	return visited, acc


# brute force
def generate_lines_variants(lines):
	for i, line in enumerate(lines):
		if line.startswith("jmp"):
			repl = "nop"
		elif line.startswith("nop"):
			repl = "jmp"
		else:
			continue
		yield lines[:i] + [repl + lines[i][3:]] + lines[i+1:]


def compute_fixed_acc(lines):
	last = len(lines) - 1
	for variant in generate_lines_variants(lines):
		visited, acc = compute_acc(variant)
		if last in visited:
			return acc


if __name__ == "__main__":
    with open("inputs/day08.txt", "r") as f:
        lines = list(f)
    print("Part 1:", compute_acc(lines)[1])
    print("Part 2:", compute_fixed_acc(lines))

import re

# utils ---------------------------------------------------------------------------------------------------------------
def check_passport(parsed_fields, required_fields, valid_data=False):
	if valid_data:
		for field, data in parsed_fields.items():
			if field == "cid":
				continue
			try:
				predicate_result = required_fields[field](data)
			except Exception as err:
				return False
			if not predicate_result:
				return False
	return set(parsed_fields) - {"cid"} == set(required_fields)


# code ----------------------------------------------------------------------------------------------------------------
with open("inputs/day4.txt", "r") as f:
    lines = list(f)

required_fields = {
    "byr": lambda data: 1920 <= int(data) <= 2002,
    "iyr": lambda data: 2010 <= int(data) <= 2020,
    "eyr": lambda data: 2020 <= int(data) <= 2030,
    "hgt": lambda data: (150 <= int(data[:-2]) <= 193 if data.endswith("cm")
                         else 59 <= int(data[:-2]) <= 76 if data.endswith("in") 
                         else False),
    "hcl": lambda data: re.match("#[a-f0-9]{6}", data) is not None,
    "ecl": lambda data: data in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda data: len(data) == 9 and all(n.isdigit() for n in data),
}

# Part 1
parsed_fields = []
valids = 0
for line in lines + ["\n"]:
	if line == "\n":
		valids += check_passport(parsed_fields, required_fields)
		parsed_fields = []
		continue
	for match in re.finditer(r"[a-zA-Z]{3}:", line):
		parsed_fields.append(match.group(0)[:3])

print("Part 1", valids)

# Part 2
parsed_fields = {}
valids = 0
for line in lines + ["\n"]:
	if line == "\n":
		valids += check_passport(parsed_fields, required_fields, valid_data=True)
		parsed_fields = {}
		continue
	for match in re.finditer(r"([a-zA-Z]{3}):(#?\w*)", line):
		parsed_fields[match.group(1)[:3]] = match.group(2)

print("Part 2", valids)
with open("inputs/day2.txt", "r") as f:
    lines = list(iter(f))

# Part 1
valids = 0
for line in lines:
    minmax, letter, password = line.split(" ")
    min_occ, max_occ = [int(n) for n in minmax.split("-")]
    letter = letter[0]
    valids += min_occ <= password.count(letter) <= max_occ

print("Part 1", valids)

# Part 2
valids = 0
for line in lines:
    minmax, letter, password = line.split(" ")
    min_pos, max_pos = [int(n) for n in minmax.split("-")]
    letter = letter[0]
    valids += ((password[min_pos-1] == letter) + (password[max_pos-1] == letter)) == 1

print("Part 2", valids)

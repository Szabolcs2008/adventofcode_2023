input_file = "../../puzzle.input/day4.txt"

with open(input_file, "r") as file:
    lines = file.read().split("\n")

lines = list(line[line.index(":")+1:].strip() for line in lines)
lines = list(line.split("|") for line in lines)
lines = list(list(line_part.split(" ") for line_part in line) for line in lines)
lines = list(list(list(item for item in line_part if item != "") for line_part in line) for line in lines)

matches_per_line = []
instances = []

for line in lines:
    matches = 0
    winning = list(int(number) for number in line[0])
    numbers = list(int(num) for num in line[1])
    for number in numbers:
        if number in winning:
            matches += 1
    matches_per_line.append(matches)
    instances.append(1)

last_matches = 0


for idx in range(len(matches_per_line)):
    matches = matches_per_line[idx]
    for i in range(idx+1, idx+matches+1):
        instances[i] += instances[idx]







print(sum(instances))

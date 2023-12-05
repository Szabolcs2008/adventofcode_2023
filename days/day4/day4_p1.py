input_file = "../../puzzle.input/day4.txt"

with open(input_file, "r") as file:
    lines = file.read().split("\n")

lines = list(line[line.index(":")+1:].strip() for line in lines)
lines = list(line.split("|") for line in lines)
lines = list(list(line_part.split(" ") for line_part in line) for line in lines)
lines = list(list(list(item for item in line_part if item != "") for line_part in line) for line in lines)

sum = 0

for line in lines:
    matches = 0
    winning = list(int(number) for number in line[0])
    numbers = list(int(num) for num in line[1])
    for number in numbers:
        if number in winning:
            matches += 1
    if matches == 0:
        points = 0
    else:
        points = 2**(matches-1)

    sum += points

    print(points)

print(sum)
input_file = "../../puzzle.input/day1.txt"

with open(input_file, "r") as file:
    raw_data = file.read()

lines = raw_data.split("\n")

lines_numbers = []

sum = 0

for line in lines:
    numbers = []
    idx = 0
    for char in line:

        if char.isnumeric():
            numbers.append(char)
        else:
            if line[idx:idx+3].casefold() == "one":
                numbers.append("1")
            elif line[idx:idx+3].casefold() == "two":
                numbers.append("2")
            elif line[idx:idx+5].casefold() == "three":
                numbers.append("3")
            elif line[idx:idx+4].casefold() == "four":
                numbers.append("4")
            elif line[idx:idx+4].casefold() == "five":
                numbers.append("5")
            elif line[idx:idx+3].casefold() == "six":
                numbers.append("6")
            elif line[idx:idx+5].casefold() == "seven":
                numbers.append("7")
            elif line[idx:idx+5].casefold() == "eight":
                numbers.append("8")
            elif line[idx:idx+4].casefold() == "nine":
                numbers.append("9")

        idx += 1
    print(numbers)
    lines_numbers.append(numbers)

for item in lines_numbers:
    num_str = ""
    num_str += item[0]
    num_str += item[-1]
    sum += int(num_str)

print(sum)
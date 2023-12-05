input_file = "../../puzzle.input/day3.txt"

with open(input_file, "r") as f:
    lines = f.read().split("\n")

line_id = 0
nums = []
for line in lines:
    tmp = []
    char_id = 0
    for char in line:
        if char != ".":
            if char.isnumeric():
                # is neighbour a number?
                try:
                    if line[char_id-1].isnumeric():
                        tmp[-1][1] += char
                        tmp[-1][2].append(char_id)
                    else:
                        tmp.append([False, char, [char_id], ["", 0]])
                except:
                    pass

        char_id += 1
    nums.append(tmp)

for idx in range(len(lines)):
    num_tmp = nums[idx]
    try:
        upper_line = lines[idx - 1]
    except:
        upper_line = None
    try:
        lower_line = lines[idx + 1]
    except:
        lower_line = None
    line = lines[idx]
    for num_idx in range(len(num_tmp)):
        places = num_tmp[num_idx][2]
        for place in places:
            if (upper_line != None) and (place != 0) and (place != len(upper_line) - 1) and upper_line[place-1] != "." and not upper_line[place-1].isnumeric():
                num_tmp[num_idx][0] = True
            if (upper_line != None) and (place != 0) and (place != len(upper_line) - 1) and upper_line[place] != "." and not upper_line[place].isnumeric():
                num_tmp[num_idx][0] = True
            if (upper_line != None) and (place != 0) and (place != len(upper_line) - 1) and upper_line[place+1] != "." and not upper_line[place+1].isnumeric():
                num_tmp[num_idx][0] = True
            if (place != 0) and (place != len(line) - 1) and line[place-1] != "."and not line[place-1].isnumeric():
                num_tmp[num_idx][0] = True
            if (place != 0) and (place != len(line) - 1) and line[place+1] != "." and not line[place+1].isnumeric():
                num_tmp[num_idx][0] = True
            if (lower_line != None) and (place != 0) and (place != len(lower_line) - 1) and lower_line[place-1] != "." and not lower_line[place-1].isnumeric():
                num_tmp[num_idx][0] = True
            if (lower_line != None) and (place != 0) and (place != len(lower_line) - 1) and lower_line[place] != "." and not lower_line[place].isnumeric():
                num_tmp[num_idx][0] = True
            if (lower_line != None) and (place != 0) and (place != len(lower_line) - 1) and lower_line[place+1] != "." and not lower_line[place+1].isnumeric():
                num_tmp[num_idx][0] = True

sum = 0

for n in nums:
    for num in n:
        if num[0] == True:
            print(num[1])
            sum += int(num[1])

print(sum)
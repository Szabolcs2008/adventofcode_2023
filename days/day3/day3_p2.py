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
                        tmp.append([False, char, [char_id], []])
                except:
                    pass

        char_id += 1
    nums.append(tmp)

symbols = []
symbol_count = []

for idx in range(len(lines)):
    try:
        upper_line = lines[idx - 1]
    except:
        upper_line = None
    try:
        lower_line = lines[idx + 1]
    except:
        lower_line = None
    line = lines[idx]
    for num_idx in range(len(nums[idx])):
        places = nums[idx][num_idx][2]
        for place in places:
            if (upper_line != None) and (place != 0) and (place != len(upper_line) - 1) and upper_line[place-1] != "." and not upper_line[place-1].isnumeric():
                nums[idx][num_idx][0] = True
                symbol_data = [upper_line[place-1], place-1, idx-1]
                if symbol_data not in nums[idx][num_idx][3]:
                    nums[idx][num_idx][3].append(symbol_data)
                    if symbol_data not in symbols:
                        symbols.append(symbol_data)
            if (upper_line != None) and (place != 0) and (place != len(upper_line) - 1) and upper_line[place] != "." and not upper_line[place].isnumeric():
                nums[idx][num_idx][0] = True
                symbol_data = [upper_line[place], place, idx-1]
                if symbol_data not in nums[idx][num_idx][3]:
                    nums[idx][num_idx][3].append(symbol_data)
                    if symbol_data not in symbols:
                        symbols.append(symbol_data)
            if (upper_line != None) and (place != 0) and (place != len(upper_line) - 1) and upper_line[place+1] != "." and not upper_line[place+1].isnumeric():
                nums[idx][num_idx][0] = True
                symbol_data = [upper_line[place + 1], place + 1, idx-1]
                if symbol_data not in nums[idx][num_idx][3]:
                    nums[idx][num_idx][3].append(symbol_data)
                    if symbol_data not in symbols:
                        symbols.append(symbol_data)
            if (place != 0) and (place != len(line) - 1) and line[place-1] != "."and not line[place-1].isnumeric():
                nums[idx][num_idx][0] = True
                symbol_data = [line[place - 1], place - 1, idx]
                if symbol_data not in nums[idx][num_idx][3]:
                    nums[idx][num_idx][3].append(symbol_data)
                    if symbol_data not in symbols:
                        symbols.append(symbol_data)
            if (place != 0) and (place != len(line) - 1) and line[place+1] != "." and not line[place+1].isnumeric():
                nums[idx][num_idx][0] = True
                symbol_data = [line[place + 1], place + 1, idx]
                if symbol_data not in nums[idx][num_idx][3]:
                    nums[idx][num_idx][3].append(symbol_data)
                    if symbol_data not in symbols:
                        symbols.append(symbol_data)
            if (lower_line != None) and (place != 0) and (place != len(lower_line) - 1) and lower_line[place-1] != "." and not lower_line[place-1].isnumeric():
                nums[idx][num_idx][0] = True
                symbol_data = [lower_line[place - 1], place - 1, idx+1]
                if symbol_data not in nums[idx][num_idx][3]:
                    nums[idx][num_idx][3].append(symbol_data)
                    if symbol_data not in symbols:
                        symbols.append(symbol_data)
            if (lower_line != None) and (place != 0) and (place != len(lower_line) - 1) and lower_line[place] != "." and not lower_line[place].isnumeric():
                nums[idx][num_idx][0] = True
                symbol_data = [lower_line[place], place, idx+1]
                if symbol_data not in nums[idx][num_idx][3]:
                    nums[idx][num_idx][3].append(symbol_data)
                    if symbol_data not in symbols:
                        symbols.append(symbol_data)
            if (lower_line != None) and (place != 0) and (place != len(lower_line) - 1) and lower_line[place+1] != "." and not lower_line[place+1].isnumeric():
                nums[idx][num_idx][0] = True
                symbol_data = [lower_line[place + 1], place + 1, idx+1]
                if symbol_data not in nums[idx][num_idx][3]:
                    nums[idx][num_idx][3].append(symbol_data)
                    if symbol_data not in symbols:
                        symbols.append(symbol_data)


sum = 0

sym_adj = []
for sym in symbols:
    sym_adj.append([sym, []])
    for n in nums:
        for num in n:
            if sym in num[3]:
                sym_adj[-1][1].append(num)

for sym in sym_adj:
    if len(sym[1]) == 2:
        sum += int(sym[1][0][1]) * int(sym[1][1][1])

print(sum)
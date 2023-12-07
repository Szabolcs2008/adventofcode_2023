input_file = "../../puzzle.input/day6.txt"

with open(input_file, 'r') as file:
    rows = file.read().split("\n")

times = list(item for item in rows[0].split() if item != "" and item.casefold() != "time:")
distances = list(item for item in rows[1].split() if item != "" and item.casefold() != "distance:")
pairs = list([int(times[i]), int(distances[i])] for i in range(min([len(times), len(distances)])))

record_could_be_beaten = {}

for data_pair in pairs:
    record_could_be_beaten[f"r_{pairs.index(data_pair)}"] = 0
    t_all = data_pair[0]
    record = data_pair[1]

    for button_pressed_ms in range(0, t_all+1):
        v = button_pressed_ms
        t_rem = t_all - button_pressed_ms
        s = t_rem * v
        if s > record:
            record_could_be_beaten[f"r_{pairs.index(data_pair)}"] += 1


ans = 1
for item in record_could_be_beaten:
    ans *= record_could_be_beaten[item]

print(ans)


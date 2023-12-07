input_file = "../../puzzle.input/day6.txt"

with open(input_file, 'r') as file:
    rows = file.read().split("\n")

t_max = int(rows[0].replace(" ", "").replace("Time:", ""))
record = int(rows[1].replace(" ", "").replace("Distance:", ""))

record_could_be_beaten = 0

for button_pressed_ms in range(0, t_max+1):
    v = button_pressed_ms
    t_rem = t_max - button_pressed_ms
    s = t_rem * v
    if s > record:
        record_could_be_beaten += 1

print(record_could_be_beaten)

input_file = "../../puzzle.input/day2.txt"

with open(input_file, "r") as file:
    raw_data = file.read()

lines = raw_data.split("\n")

sum = 0

game_data = []

for line in lines:
    tmp = []
    gameId = line.split(":")[0]
    tmp.append(gameId)
    gameData = line.split(":")[1].strip()
    subsets = gameData.split(";")
    for subset in subsets:
        t = []
        cubes = subset.strip().split(",")
        for cube in cubes:
            cube_data = cube.strip().split(" ")
            t.append([cube_data[1], cube_data[0]])
        tmp.append(t)
    game_data.append(tmp)
    print(tmp)

def getPower(game):
    red = []
    green = []
    blue = []
    data = game[1:]
    for subset in data:
        for cube in subset:
            if cube[0] == "red":
                red.append(int(cube[1]))
            elif cube[0] == "green":
                green.append(int(cube[1]))
            elif cube[0] == "blue":
                blue.append(int(cube[1]))
    return max(red) * max(green) * max(blue)

for game in game_data:
    power = getPower(game)
    print(power)
    sum += power
print(sum)
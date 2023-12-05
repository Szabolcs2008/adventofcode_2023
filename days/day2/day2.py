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


def isPossible(game):
    data = game[1:]
    for subset in data:
        for cube in subset:
            if cube[0] == "red":
                if int(cube[1]) > 12:
                    return False
            elif cube[0] == "green":
                if int(cube[1]) > 13:
                    return False
            elif cube[0] == "blue":
                if int(cube[1]) > 14:
                    return False
    return True

for item in game_data:
    id = int(item[0].split()[1])
    possible = isPossible(item)
    print([id, possible])
    if possible:
        sum += id
    else:
        pass

print(sum)

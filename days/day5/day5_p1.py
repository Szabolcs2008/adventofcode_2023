input_file = "../../puzzle.input/day5.txt"

with open(input_file, "r") as file:
    file_data = file.read().split("\n")
    seeds = list(int(item) for item in file_data[0].split()[1:])
    seed_to_soil_idx = file_data.index("seed-to-soil map:")
    soil_to_fertiliser_idx = file_data.index("soil-to-fertilizer map:")
    fertiliser_to_water_idx = file_data.index("fertilizer-to-water map:")
    water_to_light_idx = file_data.index("water-to-light map:")
    light_to_temperature_idx = file_data.index("light-to-temperature map:")
    temperature_to_humidity_idx = file_data.index("temperature-to-humidity map:")
    humidity_to_location_idx = file_data.index("humidity-to-location map:")

seed_to_soil = list(item.split() for item in file_data[seed_to_soil_idx+1:soil_to_fertiliser_idx-1])
soil_to_fertiliser = list(item.split() for item in file_data[soil_to_fertiliser_idx+1:fertiliser_to_water_idx-1])
fertiliser_to_water = list(item.split() for item in file_data[fertiliser_to_water_idx+1:water_to_light_idx-1])
water_to_light = list(item.split() for item in file_data[water_to_light_idx+1:light_to_temperature_idx-1])
light_to_temperature = list(item.split() for item in file_data[light_to_temperature_idx+1:temperature_to_humidity_idx-1])
temperature_to_humidity = list(item.split() for item in file_data[temperature_to_humidity_idx+1:humidity_to_location_idx-1])
humidity_to_location = list(item.split() for item in file_data[humidity_to_location_idx+1:])

mappings_list = [seed_to_soil, soil_to_fertiliser, fertiliser_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

data = {}

for seed in seeds:
    data[seed] = int(seed)
    for mappings in mappings_list:
        found = False

        for mapping in mappings:
            if found == True:
                continue
            dst_start = mapping[0]
            src_start = mapping[1]
            idx_range = mapping[2]
            if data[seed] in range(int(src_start), int(src_start)+int(idx_range)):
                data[seed] = int(data[seed]) + (int(dst_start) - int(src_start))
                found = True
                print(seed, f"{data[seed]} = {int(data[seed]) - (int(dst_start) - int(src_start))} + ({(int(dst_start))} - {int(src_start)})", [dst_start, src_start, idx_range], True)
                break
        if found == False:
            data[seed] = data[seed]
            print(seed, data[seed], False)


print(data)
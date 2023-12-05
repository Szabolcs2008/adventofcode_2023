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

seed_to_soil = file_data[seed_to_soil_idx+1:soil_to_fertiliser_idx-1]
soil_to_fertiliser = file_data[soil_to_fertiliser_idx+1:fertiliser_to_water_idx-1]
fertiliser_to_water = file_data[fertiliser_to_water_idx+1:water_to_light_idx-1]
water_to_light = file_data[water_to_light_idx+1:light_to_temperature_idx-1]
light_to_temperature = file_data[light_to_temperature_idx+1:temperature_to_humidity_idx-1]
temperature_to_humidity = file_data[temperature_to_humidity_idx+1:humidity_to_location_idx-1]
humidity_to_location = file_data[humidity_to_location_idx+1:]


print(seeds)
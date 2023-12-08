def run():
    seeds = []
    seed_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []

    maps = [
        seed_soil,
        soil_fertilizer,
        fertilizer_water,
        water_light,
        light_temperature,
        temperature_humidity,
        humidity_location,
    ]



    with open("input.txt", "r") as f:
        line = f.readline()
        seeds = [int(seed) for seed in line.split()[1:]]

        map_idx = -1
        while line != '':
            line = f.readline()

            if line == "\n":
                line = f.readline()
                print(line)
                map_idx += 1
                continue

            maps[map_idx].append(tuple(int(n) for n in line.split()))


    print(maps[0])

    

if __name__ == "__main__":
    run()
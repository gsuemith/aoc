from sys import maxsize
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
        line = f.readline()
        map_idx = -1

        while line != '':

            if line == "\n":
                line = f.readline()
                line = f.readline()
                map_idx += 1
                continue

            maps[map_idx].append(tuple(int(n) for n in line.split()))
            line = f.readline()

    for map in maps:
        map.sort(key=lambda x: x[1])

    lowest = max(a + c for a,b,c in maps[-1])
    maxint = lowest
    print(lowest)

    for i in range(len(seeds) // 2):
        start, rnge = seeds[2*i], seeds[2*i+1]
        seed = start
        print(start, rnge, end="\n\n")
        while seed < start + rnge:
            output = seed
            boundaries = []
            for map in maps:
                input = output
                output, bound = transform(input, map)
                boundaries.append(bound)
            lowest = min(lowest, output)
            seed += min(boundaries)
            print(seed, output, lowest)
        

    print(lowest)

def transform(input, map):
    idx = bin_search(input, map)

    dest, source, rnge = map[idx]

    if input - source >= rnge:
        return input, (map[idx+1][1] - input) if idx + 1 < len(map) else max(m[1] + m[2] for m in map)
    
    output = input - source + dest
    return output, source + rnge - input

def bin_search(input, map):
    left = 0
    right = len(map) - 1
    mid = (left + right) // 2

    while left < right - 1:
        source = map[mid][1]
        if input < source:
            right = mid - 1
            mid = (left + right) // 2
        else:
            left = mid
            mid = (left + right) // 2
    return right if input >= map[right][1] else mid

    
if __name__ == "__main__":
    run()
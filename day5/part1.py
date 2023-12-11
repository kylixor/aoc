from dataclasses import dataclass


file = open('day5/input.txt', 'r')
lines = file.read().splitlines()

@dataclass
class StupidUnitMap:
    dst_start: int
    src_start: int
    steps: int

def parse_maps(input_str: list[str]) -> list[StupidUnitMap]:
    unit_map = []
    for line in input_str:
        values = line.split(' ')
        dst_start = int(values[0])
        src_start = int(values[1])
        steps = int(values[2])
        unit = StupidUnitMap(dst_start, src_start, steps)
        unit_map.append(unit)
    return sorted(unit_map, key=lambda x: x.src_start)

def converter(input_unit: int, unit_map: list[StupidUnitMap]) -> int:
    for value_range in unit_map:
        if input_unit >= value_range.src_start and input_unit <= value_range.src_start + value_range.steps:
            return input_unit + value_range.dst_start - value_range.src_start
        elif input_unit > value_range.src_start:
            continue
    return input_unit

seeds = lines[0].split(':')[1].strip().split(' ')
seeds = [int(x) for x in seeds]

seed_soil_map = parse_maps(lines[3:18])
soil_fertilizer_map = parse_maps(lines[21:38])
fertilizer_water_map = parse_maps(lines[41:80])
water_light_map = parse_maps(lines[83:98])
light_temperature_map = parse_maps(lines[101:140])
temperature_humidity_map = parse_maps(lines[143:180])
humidity_location_map = parse_maps(lines[183:218])

locations = []
for seed in seeds:
    soil = converter(seed, seed_soil_map)
    fertilizer = converter(soil, soil_fertilizer_map)
    water = converter(fertilizer, fertilizer_water_map)
    light = converter(water, water_light_map)
    temperature = converter(light, light_temperature_map)
    humidity = converter(temperature, temperature_humidity_map)
    location = converter(humidity, humidity_location_map)
    locations.append(location)
print(min(locations))
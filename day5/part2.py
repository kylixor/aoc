from functools import reduce

seeds, *mappings = open('day5/input.txt').read().split('\n\n')
seeds = list(map(int, seeds.split()[1:]))

def lookup(inputs, mapping):
    for start, length in inputs:
        while length > 0:
            for m in mapping.split('\n')[1:]:
                dst, src, len = map(int, m.split())
                delta = start - src
                if delta in range(len):
                    len = min(len - delta, length)
                    yield (dst + delta, len)
                    start += len
                    length -= len
                    break
            else: yield (start, length); break

print(*[min(reduce(lookup, mappings, s))[0] for s in [
    zip(seeds, [1] * len(seeds)),
    zip(seeds[0::2], seeds[1::2])]])


# from dataclasses import dataclass

# file = open('day5/input.txt', 'r')
# lines = file.read().splitlines()

# @dataclass
# class StupidUnitMap:
#     dst_start: int
#     src_start: int
#     steps: int

# @dataclass
# class Seed:
#     start: int
#     end: int

# def parse_maps(input_str: list[str]) -> list[StupidUnitMap]:
#     unit_map = []
#     for line in input_str:
#         values = line.split(' ')
#         dst_start = int(values[0])
#         src_start = int(values[1])
#         steps = int(values[2])
#         unit = StupidUnitMap(dst_start, src_start, steps)
#         unit_map.append(unit)
#     return sorted(unit_map, key=lambda x: x.src_start)

# def converter(input_unit: Seed, unit_map: list[StupidUnitMap]) -> list[int]:
#     for value_range in unit_map:
#         if input_unit >= value_range.src_start and input_unit <= value_range.src_start + value_range.steps:
#             return input_unit + value_range.dst_start - value_range.src_start
#         elif input_unit > value_range.src_start:
#             continue
#     return input_unit

# seeds = lines[0].split(':')[1].strip().split(' ')
# seeds = [int(x) for x in seeds]
# seeds = [Seed(x, seeds[idx + 1]) for idx, x in enumerate(seeds) if not idx % 2]

# seed_soil_map = parse_maps(lines[3:18])
# soil_fertilizer_map = parse_maps(lines[21:38])
# fertilizer_water_map = parse_maps(lines[41:80])
# water_light_map = parse_maps(lines[83:98])
# light_temperature_map = parse_maps(lines[101:140])
# temperature_humidity_map = parse_maps(lines[143:180])
# humidity_location_map = parse_maps(lines[183:218])

# locations = []
# for seed in seeds:
#     soil = converter(seed, seed_soil_map)
#     fertilizer = converter(soil, soil_fertilizer_map)
#     water = converter(fertilizer, fertilizer_water_map)
#     light = converter(water, water_light_map)
#     temperature = converter(light, light_temperature_map)
#     humidity = converter(temperature, temperature_humidity_map)
#     location = converter(humidity, humidity_location_map)
#     locations.append(location)
# print(min(locations))
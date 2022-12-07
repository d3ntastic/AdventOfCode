import os
import numpy

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        map = f.read().splitlines()
    return [list(x) for x in map]

def get_adjacent_tiles(input, row_id, col_id, return_coords=False):
    adjacent_tiles = []
    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            if row_offset == 0 and col_offset == 0 or row_offset == col_offset or row_offset == -col_offset:
                continue
            if (row_id + row_offset) < 0 or (row_id + row_offset) >= len(input):
                continue
            if (col_id + col_offset) < 0 or (col_id + col_offset) >= len(input[0]):
                continue
            if (return_coords):
                adjacent_tiles.append([row_id + row_offset, col_id + col_offset])
            else:
                adjacent_tiles.append(input[row_id + row_offset][col_id + col_offset])
    return adjacent_tiles

def get_basin(input, row_id, col_id):
    elements_in_basin = [[row_id, col_id]]
    grown = True
    i = 0 
    while grown:
        i += 1
        grown = False
        for element_in_basin in elements_in_basin:
            adjacent_tiles = get_adjacent_tiles(input, element_in_basin[0], element_in_basin[1], True)
            for adjacent_tile in adjacent_tiles:
                if input[adjacent_tile[0]][adjacent_tile[1]] == '9' or adjacent_tile in elements_in_basin:
                    continue
                else:
                    grown = True
                    elements_in_basin.append(adjacent_tile)
    return elements_in_basin
            

def part_one():
    input = read_input('./input.txt')
    low_points_risk = []
    for row_id, row in enumerate(input):
        for col_id, element in enumerate(row):
            adjacent_tiles = get_adjacent_tiles(input, row_id, col_id)
            is_lowpoint = True
            for tile in adjacent_tiles:
                if int(tile) <= int(element):
                    is_lowpoint = False
                    break
            if is_lowpoint:
                low_points_risk.append(int(element) + 1)

    return sum(low_points_risk)

def part_two():
    input = read_input('./input.txt')
    already_seen = []
    basin_sizes = []
    for row_id, row in enumerate(input):
        for col_id, element in enumerate(row):
            if ([row_id, col_id] not in already_seen and element != '9'):
                current_basin = get_basin(input, row_id, col_id)
                current_basin_size = len(current_basin)
                for element in current_basin:
                    already_seen.append(element)
                basin_sizes.append(current_basin_size)
    basin_sizes.sort(reverse=True)
    return numpy.prod(basin_sizes[:3])

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
import os

already_flashed = []

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        map = f.read().splitlines()
    return [[int(x) for x in lines] for lines in map]

def format_input(input):
    return '\n'.join([''.join(map(str, line)) for line in input])

def get_adjacent_tiles(input, row_id, col_id, return_coords=False):
    adjacent_tiles = []
    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            if row_offset == 0 and col_offset == 0:
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

def flash_all(input, row_id, col_id):
    flashes = 1
    global already_flashed
    adjacent_tiles = get_adjacent_tiles(input, row_id, col_id, True)
    for adjacent_tile in adjacent_tiles:
        if adjacent_tile in already_flashed:
            continue
        input[adjacent_tile[0]][adjacent_tile[1]] += 1
        if input[adjacent_tile[0]][adjacent_tile[1]] > 9:
            already_flashed.append([adjacent_tile[0], adjacent_tile[1]])
            input, sub_flashes = flash_all(input, adjacent_tile[0], adjacent_tile[1])

            flashes += sub_flashes
    
    input[row_id][col_id] = 0
    return input, flashes

def part_one():
    input = read_input('./input.txt')
    flash_sum = 0
    print("Before: ", input)
    for i in range(100):
        global already_flashed
        already_flashed = []
        for y in range(len(input)):
            for x in range(len(input[y])):
                input[y][x] += 1
        for y in range(len(input)):
            for x in range(len(input[y])):
                if input[y][x] > 9:
                    already_flashed.append([y, x])
                    input, flashes = flash_all(input, y, x)

                    flash_sum += flashes
        print("After " + str(i + 1))
        print(format_input(input))
    return flash_sum

def part_two():
    input = read_input('./input.txt')
    flash_sum = 0
    print("Before: ", input)
    global already_flashed
    i = 0
    while len(already_flashed) < len(input) * len(input[0]):
        i += 1
        already_flashed = []
        for y in range(len(input)):
            for x in range(len(input[y])):
                input[y][x] += 1
        for y in range(len(input)):
            for x in range(len(input[y])):
                if input[y][x] > 9:
                    already_flashed.append([y, x])
                    input, flashes = flash_all(input, y, x)

                    flash_sum += flashes
        print("Today flashed " + str(i), len(already_flashed))
    return i

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
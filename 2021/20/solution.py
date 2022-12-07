import os
from functools import reduce
from operator import mul

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    algorithm = input[0]
    image = [list(x) for x in input[2:]]
    return algorithm, image


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def extend_image(image, replace_value = '.'):
    for _ in range(2):
        image.insert(0, [replace_value for _ in range(len(image[0]))])
        image.append([replace_value for _ in range(len(image[0]))])
        for row in image:
            row.insert(0, replace_value)
            row.append(replace_value)
    return image

def get_adjacents(image, x, y, replace_value):
    adjacents = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (x == 0 or y == 0 or x == len(image) - 1 or y == len(image[0]) - 1):
                adjacents.append(replace_value)
            else:
                adjacents.append(image[i][j])
    return adjacents

def part_one():
    algorithm, image = read_input('./input.txt')
    image = extend_image(image)
    print_matrix(image)
    print("")
    for c in range(2):
        replace_value = '#' if algorithm[0] == '#' and c % 2 == 1 else '.'
        extend_value = '#' if algorithm[0] == '#' and c % 2 == 0 else '.'
        new_image = [["." for _ in range(len(image[0]))] for _ in range(len(image))]
        for row_id, row in enumerate(image):
            for col_id, col in enumerate(row):
                adjacents = get_adjacents(image, row_id, col_id, replace_value)
                result = []
                for adjacent_row in adjacents:
                    for adjacent in adjacent_row:
                        result.append(0 if adjacent == '.' else 1)
                result_binary = ''.join(map(str, result))
                result_number = int(result_binary, 2)
                new_image[row_id][col_id] = algorithm[result_number]
        image = new_image.copy()
        image = extend_image(image, extend_value)
        print_matrix(image)
        print("")
    
    endnumber = 0
    for row in image:
        for col in row:
            if col == '#':
                endnumber += 1
    return endnumber

def part_two():
    algorithm, image = read_input('./testinput.txt')
    image = extend_image(image)
    print_matrix(image)
    print("")
    for c in range(50):
        replace_value = '#' if algorithm[0] == '#' and c % 2 == 1 else '.'
        extend_value = '#' if algorithm[0] == '#' and c % 2 == 0 else '.'
        new_image = [["." for _ in range(len(image[0]))] for _ in range(len(image))]
        for row_id, row in enumerate(image):
            for col_id, col in enumerate(row):
                adjacents = get_adjacents(image, row_id, col_id, replace_value)
                result = []
                for adjacent_row in adjacents:
                    for adjacent in adjacent_row:
                        result.append(0 if adjacent == '.' else 1)
                result_binary = ''.join(map(str, result))
                result_number = int(result_binary, 2)
                new_image[row_id][col_id] = algorithm[result_number]
        image = new_image.copy()
        image = extend_image(image, extend_value)
        print("Current run: ", c)
    print_matrix(image)
    endnumber = 0
    for row in image:
        for col in row:
            if col == '#':
                endnumber += 1
    return endnumber

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
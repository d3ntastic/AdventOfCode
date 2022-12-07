import os

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    dots = [x.split(',') for x in input if ',' in x]
    folds = [x.split(' ')[2].split("=") for x in input if 'fold along' in x]
    return dots, folds

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def create_matrix(dots):
    highest_x = 0
    highest_y = 0
    for dot in dots:
        x = int(dot[0])
        y = int(dot[1])
        if x > highest_x:
            highest_x = x
        if y > highest_y:
            highest_y = y
    matrix = [['.' for x in range(highest_x + 1)] for y in range(highest_y + 1)]
    for dot in dots:
        x = int(dot[0])
        y = int(dot[1])
        matrix[y][x] = '#'
    return matrix

def count_dots(matrix):
    dot_count = 0
    for row in matrix:
        for dot in row:
            if dot == '#':
                dot_count += 1
    return dot_count

def solution(part):
    dots, folds = read_input('./funinput.txt')
    matrix = create_matrix(dots)
    i = 0
    for fold in folds:
        if i > 0 and part == 1: continue
        i += 1
        print(f'Fold {i} of {len(folds)}.\n')
        fold_line = int(fold[1])
        if fold[0] == 'y':
            sub_matrix_1 = matrix[:fold_line]
            sub_matrix_2 = matrix[fold_line + 1:]
            for row_id, row in enumerate(sub_matrix_2):
                for col_id, col in enumerate(row):
                    if col == '#':
                        sub_matrix_1[len(sub_matrix_1) - 1 - row_id][col_id] = col
            matrix = sub_matrix_1
        if fold[0] == 'x':
            sub_matrix_1 = [row[:fold_line] for row in matrix]
            sub_matrix_2 = [row[fold_line + 1:] for row in matrix]
            for row_id, row in enumerate(sub_matrix_2):
                for col_id, col in enumerate(row):
                    if col == '#':
                        sub_matrix_1[row_id][len(sub_matrix_1[0]) - 1 - col_id] = col
            matrix = sub_matrix_1
    print_matrix(matrix)
    dot_count = count_dots(matrix)
    return dot_count


def main():
    print(solution(1))
    print(solution(2))


if __name__ == "__main__":
    main()
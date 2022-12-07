import os
import copy

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        field = f.read().splitlines()
    field_data = [list(x) for x in field]
    return field_data

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def part_one():
    field_data = read_input('./input.txt')
    counter = 0
    while True:
        skip_fields = []
        counter += 1
        initial_state = copy.deepcopy(field_data)
        is_moved = False
        for row_id, row in enumerate(field_data):
            for col_id, col in enumerate(row):
                if [row_id, col_id] in skip_fields:
                    continue
                if (col == ">"):
                    next_col_id = (col_id + 1) % len(row)
                    if (initial_state[row_id][next_col_id] == "."):
                        field_data[row_id][next_col_id] = ">"
                        field_data[row_id][col_id] = "."
                        is_moved = True
                        skip_fields.append([row_id, next_col_id])
                    continue
        initial_state = copy.deepcopy(field_data)
        for row_id, row in enumerate(field_data):
            for col_id, col in enumerate(row):
                if [row_id, col_id] in skip_fields:
                    continue
                if (col == "v"):
                    next_row_id = (row_id + 1) % len(field_data)
                    if (initial_state[next_row_id][col_id] == "."):
                        field_data[next_row_id][col_id] = "v"
                        field_data[row_id][col_id] = "."
                        is_moved = True
                        skip_fields.append([next_row_id, col_id])
                    continue
        print("Current state " + str(counter))
        if not is_moved:
            break

    return counter

def part_two():
    field_data = read_input('./input.txt')
    return "Not implemented"

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
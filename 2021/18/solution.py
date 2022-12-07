import os
import math
import numpy as np

def create_list_from_string(string):
    if string.count('[') == 1 and string.count(']') == 1:
        return list(map(int, string[1:-1].split(",")))
    if (string.count('[') == 0):
        return int(string)
    number_of_open_brackets = 0
    current_pos = 1
    for char in string[1:-1]:
        if char == '[':
            number_of_open_brackets += 1
        elif char == ']':
            number_of_open_brackets -= 1
        current_pos += 1
        if number_of_open_brackets == 0:
            return [create_list_from_string(string[1:current_pos]), create_list_from_string(string[current_pos+1:-1])]
    return "Error"


def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    input_return = [create_list_from_string(line) for line in input]
    return input_return

def add_pair(left_pair, right_pair):
    return [left_pair, right_pair]

def pair_needs_split(pair):
    # check if any element in the pair is greater than 10:
    for element in pair:
        if (type(element) == int):
            if (element >= 10):
                return True
        else:
            if (pair_needs_split(element)):
                return True

def reduce_pair(pair):
    pair = split_pair(pair)
    while True:
        while list_depth(pair) >= 5:
            pair = explode_pair(pair)
        pair = split_pair(pair)
        if list_depth(pair) < 5 and not pair_needs_split(pair):
            break
    return pair

def list_depth(l):
    if isinstance(l, list):
        return 1 + max(list_depth(item) for item in l)
    else:
        return 0

def get_path_to_deepest_pair(pair, current_path = []):
    if (type(pair) == int):
        return current_path
    left_pair = pair[0]
    right_pair = pair[1]
    left_path = current_path.copy()
    left_path.append(0)
    right_path = current_path.copy()
    right_path.append(1)
    left_path = get_path_to_deepest_pair(left_pair, left_path)
    right_path = get_path_to_deepest_pair(right_pair, right_path)
    if len(left_path) < len(right_path):
        return right_path
    return left_path

def get_path_to_leftmost_number_greater_than_10(pair, current_path = []):
    if (type(pair) == int):
        if (pair >= 10):
            return current_path
        return False
    left_pair = pair[0]
    right_pair = pair[1]
    left_path = current_path.copy()
    left_path.append(0)
    right_path = current_path.copy()
    right_path.append(1)
    left_path = get_path_to_leftmost_number_greater_than_10(left_pair, left_path)
    right_path = get_path_to_leftmost_number_greater_than_10(right_pair, right_path)
    if left_path:
        return left_path
    if right_path:
        return right_path
    return False

def update_pair_by_path(pair, path, value):
    if (type(pair) == int):
        return value
    if (len(path) == 0):
        return value
    if (path[0] == 0):
        pair[0] = update_pair_by_path(pair[0], path[1:], value)
    else:
        pair[1] = update_pair_by_path(pair[1], path[1:], value)
    return pair


def explode_pair(pair):
    if (type(pair) == int):
        return pair
    depth = list_depth(pair)
    if depth >= 5:
        deepest_path = get_path_to_deepest_pair(pair)[:-1]
        left_path = deepest_path.copy()
        right_path = deepest_path.copy()
        left_path.reverse()
        right_path.reverse()
        left_found = False
        right_found = False
        for i in range(len(left_path)):
            if (left_path[i] == 1):
                left_path[i] = 0
                left_found = True
                break
            else:
                left_path[i] = 1

        left_path.reverse()
        for i in range(len(right_path)):
            if (right_path[i] == 0):
                right_path[i] = 1
                right_found = True
                break
            else:
                right_path[i] = 0
        right_path.reverse()
        exploded_pair = pair.copy()
        for step in deepest_path:
            exploded_pair = exploded_pair[step]
        left_number = pair.copy()
        right_number = pair.copy()
        for i in range(len(left_path)):
            if (left_found and isinstance(left_number, list)):
                left_number = left_number[left_path[i]]
            if (right_found and isinstance(right_number, list)):
                right_number = right_number[right_path[i]]
        while (isinstance(right_number, list)):
            right_number = right_number[0]
            right_path.append(0)
        while (isinstance(left_number, list)):
            left_number = left_number[1]
            left_path.append(0)
        if (right_found):
            right_number += exploded_pair[1]
            pair = update_pair_by_path(pair, right_path, right_number)        
        if (left_found):
            left_number += exploded_pair[0]
            pair = update_pair_by_path(pair, left_path, left_number)          
        pair = update_pair_by_path(pair, deepest_path, 0)       
        return pair
    else:
        return pair

def split_pair(pair):
    path_to_left_most_10 = get_path_to_leftmost_number_greater_than_10(pair)
    if (path_to_left_most_10):
        split_value = pair.copy()
        for step in path_to_left_most_10:
            split_value = split_value[step]
        pair = update_pair_by_path(pair, path_to_left_most_10, [math.floor(split_value / 2), math.ceil(split_value / 2)])
        return pair
    return pair

def get_pair_magnitude(pair):
    if (type(pair) == int):
        return pair
    left_pair = pair[0]
    right_pair = pair[1]
    left_magnitude = get_pair_magnitude(left_pair)
    right_magnitude = get_pair_magnitude(right_pair)
    return 3 * left_magnitude + 2 * right_magnitude

def part_one():
    input = read_input('./input.txt')
    result = input[0]
    for c in range(len(input)):
        if c == 0:
            continue
        result = add_pair(result, input[c])
        result = reduce_pair(result)
    print(result)
    return get_pair_magnitude(result)

def part_two():
    input = read_input('./input.txt')
    biggest_magnitude = 0
    for x in range(len(input)):
        for y in range(len(input)):
            if (x == y):
                continue
            input = read_input('./input.txt')
            input_copy = input.copy()
            result = add_pair(input_copy[x], input_copy[y])
            result = reduce_pair(result[:])
            pair_magnitude = get_pair_magnitude(result)
            print(str(input_copy[x]) + " + " + str(input_copy[y]) + " = " + str(pair_magnitude) + " (" + str(get_pair_magnitude(input[0])) + ")")
            if (get_pair_magnitude(result) > biggest_magnitude):
                biggest_magnitude = get_pair_magnitude(result)
    return biggest_magnitude

def main():
    #print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
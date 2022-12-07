import os
import textwrap

def read_input_part_one(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        lines = [textwrap.wrap(line, int(len(line) / 2)) for line in f.read().splitlines()]
    return lines

def read_input_part_two(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        lines = f.read().splitlines()
    return [lines[i:i + 3] for i in range(0, len(lines), 3)]


def get_intersect(first, second):
    intersections = []
    for item in first:
        if (item in second):
            intersections.append(item)
    return list(dict.fromkeys(intersections))

def get_item_val(char):
    return ord(char) - 96 if char.islower() else ord(char) - 38

def part_one():
    input = read_input_part_one('./input.txt')
    result_array = []
    for first_com, second_com in input:
        result_array.append(get_intersect(first_com, second_com)[0])
    return sum([get_item_val(item) for item in result_array])                

def part_two():
    input = read_input_part_two('./input.txt')
    result_array = []
    for group in input:
        intersect1 = get_intersect(group[0], group[1])
        intersect2 = get_intersect(group[0], group[2])
        result_array.append(get_intersect(intersect1, intersect2)[0])
    return sum([get_item_val(item) for item in result_array])

def main():
    print(part_one())
    print(part_two())

if __name__ == "__main__":
    main()
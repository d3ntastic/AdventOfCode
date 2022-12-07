def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def part_one():
    input = read_input('input.txt')
    horizontal_position = 0
    depth = 0
    for line in input:
        [direction, distance] = line.split(' ')
        if (direction == 'forward'):
            horizontal_position += int(distance)
        if (direction == 'up'):
            depth -= int(distance)
        if (direction == 'down'):
            depth += int(distance)
    return horizontal_position * depth

def part_two():
    input = read_input('input.txt')
    horizontal_position = 0
    depth = 0
    aim = 0
    for line in input:
        [direction, distance] = line.split(' ')
        if (direction == 'forward'):
            horizontal_position += int(distance)
            depth += aim * int(distance)
        if (direction == 'up'):
            aim -= int(distance)
        if (direction == 'down'):
            aim += int(distance)
    return horizontal_position * depth

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
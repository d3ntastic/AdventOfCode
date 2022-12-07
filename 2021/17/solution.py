import os
from functools import reduce
from operator import mul

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    x_range = input[0].split(' ')[2].replace(",", "").split('=')[1].split('..')
    x_range = range(int(x_range[0]), int(x_range[1]) + 1)
    y_range = input[0].split(' ')[3].split('=')[1].split('..')
    y_range = range(int(y_range[0]), int(y_range[1]) + 1)
    return list(x_range), list(y_range)

def get_x_velocitys(x_range):
    min_x_velocity = 0
    while sum(range(min_x_velocity + 1)) < x_range[0]:
        min_x_velocity += 1
    max_x_velocity = 0
    while sum(range(max_x_velocity + 1)) < x_range[-1]:
        max_x_velocity += 1
    return min_x_velocity, max_x_velocity

def part_one():
    x_range, y_range = read_input('./input.txt')
    initial_x = 0
    initial_y = 0
    best_velocities = []
    max_y_pos = 0
    x_min_velocity, x_max_velocity = get_x_velocitys(x_range)
    for x_velocity in range(x_min_velocity, x_max_velocity + 1):
        for y_velocity in range(100):
            x_pos = initial_x
            y_pos = initial_y
            current_step = 0
            current_max_y_pos = 0
            while x_pos < x_range[-1] and y_pos > y_range[0]:
                x_pos += max([x_velocity - current_step, 0])
                y_pos += y_velocity - current_step
                current_max_y_pos = max(current_max_y_pos, y_pos)
                current_step += 1
                if (x_pos in x_range) and (y_pos in y_range):
                    if (max_y_pos < current_max_y_pos):
                        max_y_pos = current_max_y_pos
                        best_velocities = [x_velocity, y_velocity]
    return max_y_pos, best_velocities

def part_two():
    x_range, y_range = read_input('./input.txt')
    initial_x = 0
    initial_y = 0
    possible_velocities = []
    for x_velocity in range(0, x_range[-1] + 1):
        for y_velocity in range(y_range[0], 100):
            x_pos = initial_x
            y_pos = initial_y
            current_step = 0
            current_max_y_pos = 0
            while x_pos < x_range[-1] and y_pos > y_range[0]:
                x_pos += max([x_velocity - current_step, 0])
                y_pos += y_velocity - current_step
                current_max_y_pos = max(current_max_y_pos, y_pos)
                current_step += 1
                if (x_pos in x_range) and (y_pos in y_range):
                    print(y_velocity)
                    if ([x_velocity, y_velocity] not in possible_velocities):
                        possible_velocities.append([x_velocity, y_velocity])
    return len(possible_velocities)

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
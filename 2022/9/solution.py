import os

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = [e.split(" ") for e in f.read().splitlines()]
    return input

def update_position(pos, direction):
    if (direction == "L"):
        pos[0] -= 1
    if (direction == "R"):
        pos[0] += 1
    if (direction == "U"):
        pos[1] += 1
    if (direction == "D"):
        pos[1] -= 1
    return pos

def get_t_pos(tail, head, direction):
    if all([tail[i] - 1 <= head[i] <= tail[i] + 1 for i in range(2)]):
        return tail
    [tail_x, tail_y], [head_x, head_y] = tail, head
    if tail_x == head_x:
        tail[1] += int(tail_y < head_y) * 2 - 1
    elif tail_y == head_y:
        tail[0] += int(tail_x < head_x) * 2 - 1
    else:
        tail[0] += int(tail_x < head_x) * 2 - 1
        tail[1] += int(tail_y < head_y) * 2 - 1
    return tail
    

def part_one():
    input = read_input('./input.txt')
    h_pos = [0, 0]
    t_pos = [0, 0]
    visited_positions = []
    for direction, moves in input:
        moves = int(moves)
        for _ in range(0, moves):
            h_pos = update_position(h_pos, direction)
            t_pos = get_t_pos(h_pos, t_pos, direction)
            visited_positions.append(tuple(t_pos))
    return len(set(visited_positions))

def part_two():
    input = read_input('./testinput.txt')
    h_pos = [0, 0]
    t_poses = []
    for i in range(0, 9):
        t_poses.append([0, 0])
    visited_positions = []
    for direction, moves in input:
        moves = int(moves)
        for _ in range(0, moves):
            h_pos = update_position(h_pos, direction)
            for tpos_idx, tpos in enumerate(t_poses):
                if (tpos_idx == 0):
                    t_poses[tpos_idx] = get_t_pos(h_pos, tpos, direction)
                else:
                    t_poses[tpos_idx] = get_t_pos(t_poses[tpos_idx - 1], tpos, direction)
            visited_positions.append(tuple(t_poses[tpos_idx - 1]))
    return len(set(visited_positions))

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()

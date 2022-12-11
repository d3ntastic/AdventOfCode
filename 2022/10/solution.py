import os

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def update_cycle(cycle, x, total):
    cycle += 1
    noteable = [20, 60, 100, 140, 180, 220]
    if cycle in noteable:
        result = cycle * x
        print("Cycle nr. " + str(cycle) + " value: " + str(result))
        total += result
    return cycle, total


def update_cycle_sprite(cycle, sprite_pos, current_row):
    current_row += ' ' if cycle % 40 not in range(sprite_pos - 1, sprite_pos + 2) else '█'
    cycle += 1
    if (cycle % 40) == 0:
        print(current_row)
        current_row = ''

    return cycle, current_row

def part_one():
    input = read_input('./input.txt')
    cycle = 0
    x = 1
    total = 0
    for command in input:
        if command == "noop":
            cycle, total = update_cycle(cycle, x, total)
            continue
        addvalue = int(command.split(" ")[1])
        cycle, total = update_cycle(cycle, x, total)
        cycle, total = update_cycle(cycle, x, total)
        x += addvalue
    return total
        
   
def part_two():
    input = read_input('./input.txt')
    cycle = 0
    sprite_pos = 1
    current_row = ''
    for command in input:
        if command == "noop":
            cycle, current_row = update_cycle_sprite(cycle, sprite_pos, current_row)
            continue
        addvalue = int(command.split(" ")[1])
        cycle, current_row = update_cycle_sprite(cycle, sprite_pos, current_row)
        cycle, current_row = update_cycle_sprite(cycle, sprite_pos, current_row)
        sprite_pos += addvalue
        
    return ""

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()

def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [int(x) for x in lines[0].split(',')]

def part_one():
    input = read_input('input.txt')
    farest_position = max(input)
    smallest_sum = None
    current_sum = 0
    i = 0
    while i < farest_position:
        for crab_pos in input:
            current_sum += abs(crab_pos - i)
        if (smallest_sum == None or current_sum < smallest_sum):
            smallest_sum = current_sum
        current_sum = 0
        i += 1
            
    return smallest_sum

def part_two():
    input = read_input('input.txt')
    farest_position = max(input)
    smallest_sum = None
    current_sum = 0
    i = 0
    while i < farest_position:
        print(i)
        for crab_pos in input:
            for j in range(abs(crab_pos - i)):
                current_sum += j
            current_sum += abs(crab_pos - i)
        if (smallest_sum == None or current_sum < smallest_sum):
            smallest_sum = current_sum
        current_sum = 0
        i += 1
            
    return smallest_sum

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
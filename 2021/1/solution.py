def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def part_one():
    input = read_input('input.txt')
    last_input = -1
    number_of_increases = 0
    for line in input:
        current_input = int(line)
        if current_input > last_input and last_input != -1:
            number_of_increases += 1
        last_input = current_input
    return number_of_increases

def part_two():
    input = read_input('input.txt')
    last_input = -1
    number_of_increases = 0
    current_count = 0
    for index, line in enumerate(input):
        print(index, line)
        if (index >= 2):
            current_input = int(line) + int(input[index - 1]) + int(input[index - 2])
            if current_input > last_input and last_input != -1:
                number_of_increases += 1
            last_input = current_input
    return number_of_increases

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
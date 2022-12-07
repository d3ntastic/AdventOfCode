import os

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read()        
    return input

def solve(input, number_of_distinct):
    current_package = []
    for index, char in enumerate(input):
        if len(current_package) == number_of_distinct:
            current_package = current_package[1:]
        current_package.append(char)
        already_visited = []
        has_dup = False
        for element in current_package:
            if (element in already_visited):
                has_dup = True
            already_visited.append(element)
        if (len(current_package) == number_of_distinct and not has_dup):
            return index + 1 
    return 'Not found'

def part_one():
    input = read_input('./input.txt')
    return solve(input, 4)

def part_two():
    input = read_input('./input.txt')
    return solve(input, 14)

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()

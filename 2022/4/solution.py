import os

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        lines = [[[int(i) for i in assignment.split("-")] for assignment in line.split(",")] for line in f.read().splitlines()]
    return lines

def part_one():
    input = read_input('./input.txt')
    counter = 0
    for first, second in input:
         if ((first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1])):
             counter += 1
    return counter

def part_two():
    input = read_input('./input.txt')
    counter = 0
    for first, second in input:
         if ((first[0] in range(second[0], second[1] + 1)) 
             or (first[1] in range(second[0], second[1] + 1))
             or (second[0] in range(first[0], first[1] + 1))
             or (second[1] in range(first[0], first[1] + 1))):
             counter += 1
    return counter

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
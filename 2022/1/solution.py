import os

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        lines = f.read().splitlines()
        result = []
        c = 0
        for line in lines:
            if (line == ""):
                c += 1
                continue
            if (len(result) == c):
                result.append([])
            result[c].append(int(line))
    return result

def part_one():
    input = read_input('./input.txt')
    highest = 0
    for elv in input:
        if (sum(elv) > highest):
            highest = sum(elv)
    return highest

def part_two():
    input = read_input('input.txt')
    sorted = [sum(elv) for elv in input]
    sorted.sort(reverse=True)
    top3 = 0
    for i in range(0, 3):
        top3 += sorted[i]
    return top3

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
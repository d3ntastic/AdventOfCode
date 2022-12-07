def read_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    cleaned_lines = [line.replace(" -> ", ",").split(",") for line in lines]
    return cleaned_lines

def part_one():
    input = read_input('input.txt')
    # set variable a to max int:
    result_map = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in input:
        x1 = int(line[0])
        y1 = int(line[1])
        x2 = int(line[2])
        y2 = int(line[3])
        x_smaller = x1 if x1 < x2 else x2
        x_bigger = x1 if x1 > x2 else x2
        y_smaller = y1 if y1 < y2 else y2
        y_bigger = y1 if y1 > y2 else y2
        if (x1 == x2):
            while (y_smaller <= y_bigger):
                result_map[x1][y_smaller] += 1
                y_smaller += 1
        elif (y1 == y2):	
            while (x_smaller <= x_bigger):
                result_map[x_smaller][y1] += 1
                x_smaller += 1
    number_of_danger = 0
    for rows in result_map:
        for item in rows:
            if (item >= 2):
                number_of_danger += 1
    return number_of_danger

def part_two():
    input = read_input('input.txt')
    # set variable a to max int:
    result_map = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in input:
        x1 = int(line[0])
        y1 = int(line[1])
        x2 = int(line[2])
        y2 = int(line[3])
        x_smaller = x1 if x1 < x2 else x2
        x_bigger = x1 if x1 > x2 else x2
        y_smaller = y1 if y1 < y2 else y2
        y_bigger = y1 if y1 > y2 else y2
        if (x1 == x2):
            while (y_smaller <= y_bigger):
                result_map[x1][y_smaller] += 1
                y_smaller += 1
        elif (y1 == y2):	
            while (x_smaller <= x_bigger):
                result_map[x_smaller][y1] += 1
                x_smaller += 1
        else:
            x_dir = 1 if x1 < x2 else -1
            y_dir = 1 if y1 < y2 else -1
            for i in range(x_bigger - x_smaller + 1):
                result_map[x1][y1] += 1
                x1 += x_dir
                y1 += y_dir
    number_of_danger = 0
    for rows in result_map:
        for item in rows:
            if (item >= 2):
                number_of_danger += 1
    return number_of_danger

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
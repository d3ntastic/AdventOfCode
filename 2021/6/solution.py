def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [int(x) for x in lines[0].split(',')]

def part_one():
    input = read_input('input.txt')
    i = 0
    current_new_lanterfishes = 0
    while i < 80:
        for index, lanternfish in enumerate(input):
            if lanternfish == 0:
                current_new_lanterfishes += 1
                input[index] = 6
            else:
                input[index] -= 1
        for _ in range(current_new_lanterfishes):
            input.append(8)
        i += 1
        print("Tag " + str(i))
        current_new_lanterfishes = 0
            
    return len(input)

def part_two():
    input = read_input('input.txt')
    max_lanternfish = 8
    number_of_lanterfishes = [0 for _ in range(max_lanternfish + 1)]
    for lanternfish in input:
        number_of_lanterfishes[lanternfish] += 1
    i = 0
    while i < 256:
        new_sixes = 0
        new_eightes = 0
        for current_lanternfish in range(max_lanternfish + 1):
            if number_of_lanterfishes[current_lanternfish] == 0:
                continue
            old_laternfishes = number_of_lanterfishes[current_lanternfish]
            number_of_lanterfishes[current_lanternfish] = 0
            if current_lanternfish == 0:
                new_sixes += old_laternfishes
                new_eightes += old_laternfishes
            else:
                number_of_lanterfishes[current_lanternfish - 1] = old_laternfishes
    
        number_of_lanterfishes[6] += new_sixes
        number_of_lanterfishes[8] += new_eightes
        
        i += 1
        print("Tag " + str(i))
        print(number_of_lanterfishes)
    return sum(number_of_lanterfishes)

def main():
    #print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
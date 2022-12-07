def read_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return lines

def part_one():
    input = read_input('input.txt')
    numberOfOnes = [0 for i in range(0, len(input[0]))]
    numberOfZeros = [0 for i in range(0, len(input[0]))]
    for line in input:
        for index in range(len(line)):
            bit = line[index]
            if (bit == '1'):
                numberOfOnes[index] += 1
            else:
                numberOfZeros[index] += 1
    gamma_string = ''
    eps_string = ''
    for index in range(len(numberOfOnes)):
        if (numberOfOnes[index] >= numberOfZeros[index]):
            gamma_string += '1'
            eps_string += '0'
        else:
            gamma_string += '0'
            eps_string += '1'
    gamma = int(gamma_string, 2)
    eps = int(eps_string, 2)
    return gamma * eps

def part_two():
    input = read_input('input.txt')
    numberOfOnes = [0 for i in range(0, len(input[0]))]
    numberOfZeros = [0 for i in range(0, len(input[0]))]
    oxygen = 0
    co2 = 0
    filtered_list = input
    current_substring = ''
    for index in range(len(numberOfOnes)):
        numberOfOnes = [0 for i in range(0, len(input[0]))]
        numberOfZeros = [0 for i in range(0, len(input[0]))]
        for line in filtered_list:
            bit = line[index]
            if (bit == '1'):
                numberOfOnes[index] += 1
            else:
                numberOfZeros[index] += 1
        if (numberOfOnes[index] > numberOfZeros[index]):
            current_substring += '1'
        elif (numberOfOnes[index] < numberOfZeros[index]):
            current_substring += '0'
        else:
            current_substring += '1'
        temp_filtered_list = [line for line in filtered_list if line[:len(current_substring)] == current_substring]
        if (len(temp_filtered_list) > 0):
            filtered_list = temp_filtered_list

    oxygen = max([int(item, 2) for item in filtered_list])

    filtered_list = input
    current_substring = ''
    for index in range(len(numberOfOnes)):
        numberOfOnes = [0 for _ in range(0, len(input[0]))]
        numberOfZeros = [0 for _ in range(0, len(input[0]))]
        for line in filtered_list:
            bit = line[index]
            if (bit == '1'):
                numberOfOnes[index] += 1
            else:
                numberOfZeros[index] += 1
        if (numberOfOnes[index] < numberOfZeros[index]):
            current_substring += '1'
        elif (numberOfOnes[index] > numberOfZeros[index]):
            current_substring += '0'
        else:
            current_substring += '0'
        temp_filtered_list = [line for line in filtered_list if line[:len(current_substring)] == current_substring]
        if (len(temp_filtered_list) > 0):
            filtered_list = temp_filtered_list

    co2 = min([int(item, 2) for item in filtered_list])

    return oxygen * co2

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
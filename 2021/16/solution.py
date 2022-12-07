import os
from functools import reduce
from operator import mul

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    return input[0]

def hex_to_bit_string(hex_string):
    bit_string = ""
    for char in hex_string:
        bit_string += bin(int(char, 16))[2:].zfill(4)
    return bit_string

def calculate_values(bits, version_sum):
    V = int(bits[:3], 2)
    T = int(bits[3:6], 2)
    current_pos = 6
    version_sum += V
    if T == 4: #literal
        nums = []
        while True:
            first = int(bits[current_pos])
            nums.append(bits[current_pos + 1:current_pos + 5])
            current_pos += 5
            if first == 0:
                break
        literal_number = int("".join(nums), 2)
        return version_sum, literal_number, current_pos
    else: #operation
        I = int(bits[current_pos])
        current_pos += 1
        sub_numbers = []
        if I == 0: #total length of bits
            L = int(bits[current_pos:current_pos + 15], 2)
            relevant_bits = bits[current_pos + 15:current_pos + 15 + L]
            used_bits = 0
            while used_bits < L:
                version_sum, literal_number, sub_bits = calculate_values(relevant_bits[used_bits:], version_sum)
                sub_numbers.append(literal_number)
                used_bits += sub_bits
            return_bits = 7 + 15 + L
        else: #number of subpackets
            L = int(bits[current_pos:current_pos + 11], 2)
            relevant_bits = bits[current_pos + 11:]
            used_bits = 0
            runs = 0
            while runs < L:
                version_sum, literal_number, sub_bits = calculate_values(relevant_bits[used_bits:], version_sum)
                sub_numbers.append(literal_number)
                used_bits += sub_bits
                runs += 1
            return_bits = 7 + 11 + used_bits

        result = 0  
        if T == 0: #sum
            result = sum(sub_numbers)
        if T == 1: #product
            result = reduce(mul, sub_numbers, 1)
        if T == 2: #min
            result = min(sub_numbers)
        if T == 3: #max
            result = max(sub_numbers)
        if T == 5: #gt
            result = 1 if sub_numbers[0] > sub_numbers[1] else 0
        if T == 6: #lt
            result = 1 if sub_numbers[0] < sub_numbers[1] else 0
        if T == 7: #eq
            result = 1 if sub_numbers[0] == sub_numbers[1] else 0


    return version_sum, result, return_bits


def part_one():
    input = read_input('./input.txt')
    bits = hex_to_bit_string(input)
    version_sum = calculate_values(bits, 0)
    return version_sum

def part_two():
    input = read_input('./testinput.txt')
    return "Not implemented"

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
import os
import numpy

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    return input

def part_one():
    input = read_input('./input.txt')
    opening_brackets = ['(', '[', '{', '<']
    closing_brackets = [')', ']', '}', '>']
    points = {
        ')' : 3,
        ']' : 57,
        '}' : 1197,
        '>' : 25137,
    }
    opening_list = []
    error_sum = 0
    for line in input:
        for  char_index in range(len(line)):
            char = line[char_index]
            if char in opening_brackets:
                opening_list.append(char)
            elif char in closing_brackets:
                last_opening_bracket = opening_list.pop()
                if opening_brackets.index(last_opening_bracket) != closing_brackets.index(char):
                    error_sum += points.get(char)
                    break
    return error_sum
    

def part_two():
    input = read_input('./input.txt')
    opening_brackets = ['(', '[', '{', '<']
    closing_brackets = [')', ']', '}', '>']
    points = {
        ')' : 1,
        ']' : 2,
        '}' : 3,
        '>' : 4,
    }
    error_sums = []
    for line in input:
        has_error = False
        current_error_sum = 0
        opening_list = []
        for  char_index in range(len(line)):
            char = line[char_index]
            if char in opening_brackets:
                opening_list.append(char)
            elif char in closing_brackets:
                last_opening_bracket = opening_list.pop()
                if opening_brackets.index(last_opening_bracket) != closing_brackets.index(char):
                    has_error = True
                    break
        if not has_error:
            opening_list.reverse()
            for char in opening_list:
                closing_char = closing_brackets[opening_brackets.index(char)]
                current_error_sum *= 5
                current_error_sum += int(points.get(closing_char))
        if (current_error_sum != 0):
            error_sums.append(current_error_sum)
    error_sums.sort()
    return error_sums[int(len(error_sums) / 2 - 0.5)]

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
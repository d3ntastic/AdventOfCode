import os
import math

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        lines = f.read().splitlines()
    instructions = [x.split(" ") for x in lines]
    return instructions

def get_value(value, current_variables):
    if value.isdigit() or value[0] == "-":
        return int(value)
    else:
        return current_variables[value]

def runMonad(instructions, modelnumber):
    current_variables = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    number_of_inputs = 0

    for instruction in instructions:
        if instruction[0] == "inp":
            current_variables[instruction[1]] = int(modelnumber[number_of_inputs])
            number_of_inputs += 1
            continue
        if instruction[0] == "add":
            current_variables[instruction[1]] += get_value(instruction[2], current_variables) 
            continue
        if instruction[0] == "mul":
            current_variables[instruction[1]] *= get_value(instruction[2], current_variables) 
            continue
        if instruction[0] == "mod":
            if get_value(instruction[1], current_variables) < 0 or get_value(instruction[2], current_variables) <= 0:
                print("Destruction on mod")
                return False
            current_variables[instruction[1]] %= get_value(instruction[2], current_variables) 
            continue
        if instruction[0] == "div":
            if (get_value(instruction[2], current_variables) == 0):
                print("Destruction on div")
                return False
            current_variables[instruction[1]] = math.floor(current_variables[instruction[1]] / get_value(instruction[2], current_variables))
            continue
        if instruction[0] == "eql":
            current_variables[instruction[1]] = 1 if get_value(instruction[1], current_variables) == get_value(instruction[2], current_variables) else 0
            continue
    print(modelnumber)
    print(current_variables)
    return current_variables["z"]

def solve(inp, cmds):
    stack = []
    for i in range(14):
        div, chk, add = map(int, [cmds[i * 18 + x][-1] for x in [4, 5, 15]])
        if div == 1:
            stack.append((i, add))
        elif div == 26:
            j, add = stack.pop()
            inp[i] = inp[j] + add + chk
            if inp[i] > 9:
                inp[j] -= inp[i] - 9
                inp[i] = 9
            if inp[i] < 1:
                inp[j] += 1 - inp[i]
                inp[i] = 1

    return "".join(map(str, inp))

def part_one():
    instructions = read_input('./input.txt')
    return solve([9] * 14, instructions)

def part_two():
    instructions = read_input('./input.txt')
    return solve([1] * 14, instructions)

def main():
    print(part_one())
    print(part_two())

if __name__ == "__main__":
    main()
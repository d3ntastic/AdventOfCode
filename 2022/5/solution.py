import os

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        lines = f.read().splitlines()
        stack_line = ""
        number_of_crate_lines = 0
        for line in lines:
            if (any(char.isdigit() for char in line)):
                stack_line = line
                break
            number_of_crate_lines += 1
        number_of_stacks = int(stack_line.strip().split(" ")[-1])
        stacks = []
        instructions = []
        for (i, line) in enumerate(lines):
            if (i >= number_of_crate_lines):
                if (any(char.isdigit() for char in line)):
                    instructions.append([int(char) for char in line.split(" ") if char.isdigit()])
            else:
                for i in range(number_of_stacks):
                    if (i >= len(stacks)):
                        stacks.append([])
                    stacks[i].append(line[1 + i * 4].replace(" ", ""))
    correct_stacks = [[element for element in stack[::-1] if element != ""] for stack in stacks]
        
    return instructions[1:], correct_stacks

def flatten(l):
    return [item for sublist in l for item in sublist]

def move(instruction, stacks, reverse=True):
    number, from_stack, to_stack = instruction
    from_stack = from_stack - 1
    to_stack = to_stack - 1
    new_stack = []
    for (i, stack) in enumerate(stacks):
        if (i == from_stack):
            new_stack.append(stack[:-number])
        elif (i == to_stack):
            moveing = stacks[from_stack][-number:][::-1] if reverse else stacks[from_stack][-number:]
            new_stack.append(stack + moveing)
        else:
            new_stack.append(stack)
    return new_stack

def part_one():
    instructions, stacks = read_input('./input.txt')
    for instruction in instructions:
        stacks = move(instruction, stacks)
    return ''.join([stack[-1] for stack in stacks])

def part_two():
    instructions, stacks = read_input('./input.txt')
    for instruction in instructions:
        stacks = move(instruction, stacks, reverse=False)
    return ''.join([stack[-1] for stack in stacks])

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
